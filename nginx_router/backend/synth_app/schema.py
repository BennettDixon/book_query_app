import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from synth_app.models import Author, Book


class AuthorType(DjangoObjectType):
    """
        Create a GraphQL Type for our Author Model
    """
    class Meta:
        model = Author


class BookType(DjangoObjectType):
    """
        Create a GraphQL Type for our Book Model
    """
    class Meta:
        model = Book


class Query(ObjectType):
    """
        Create a GraphQL Query Type for our API
    """
    author = graphene.Field(AuthorType, id=graphene.Int())
    book = graphene.Field(BookType, id=graphene.Int())
    authors = graphene.List(AuthorType)
    books = graphene.List(BookType)

    def resolve_author(self, info, **kwargs):
        """
            graphene expects a reolver to take the graphql context
            and translate it into data for the response

            Return: Author if found, otherwise None
        """
        id = kwargs.get('id')

        if id:
            return Author.objects.get(pk=id)

        return None

    def resolve_book(self, info, **kwargs):
        """
            graphene expects a reolver to take the graphql context
            and translate it into data for the response

            Return: Book if found, otherwise None 
        """
        id = kwargs.get('id')

        if id:
            return Book.objects.get(pk=id)

        return None

    def resolve_authors(self, info, **kwargs):
        """
            fetches all of the authors
        """
        return Author.objects.all()

    def resolve_books(self, info, **kwargs):
        """
            fetches all of the books
        """
        return Book.objects.all()


class AuthorInput(graphene.InputObjectType):
    """
        The input for the author class
        aka when an author needs to be added to the db
    """
    id = graphene.ID()
    name = graphene.String()


class BookInput(graphene.InputObjectType):
    """
        The input for the book class
        aka when a book needs to be added to the db
    """
    id = graphene.ID()
    title = graphene.String()
    author = graphene.Field(AuthorInput)
    year = graphene.Int()


class CreateAuthor(graphene.Mutation):
    """
        Mutation to actually manipulate the db and graphql
        (do the actual creation)
    """
    class Arguments:
        # define the input for our static mutate method
        input = AuthorInput(required=True)

    ok = graphene.Boolean()
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        author_instance = Author(name=input.name)
        author_instance.save()
        return CreateAuthor(ok=ok, author=author_instance)


class UpdateAuthor(graphene.Mutation):
    """
        Mutation to update an instance of an author in the database using graphql
    """
    class Arguments:
        # define the input arguments for our static mutate method
        id = graphene.Int(required=True)
        input = AuthorInput(required=True)

    ok = graphene.Boolean()
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        author_instance = Author.objects.get(pk=id)
        if author_instance:
            ok = True
            author_instance.name = input.name
            author_instance.save()
        # return with status and updated instance (False/None if failed)
        return UpdateAuthor(ok=ok, author=author_instance)


class CreateBook(graphene.Mutation):
    """
        Mutation to create an instance of the book in the database using graphql
    """
    class Arguments:
        """
            define the input arguments for the static mutate method
        """
        input = BookInput(required=True)

    ok = graphene.Boolean()
    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, input=None):
        """
            Mutation method to create the new book &
                verify the author is a valid author
        """
        ok = True
        author = None
        author = Author.objects.get(pk=input.author.id)
        if author is None:
            return CreateBook(ok=False, book=None)
        book_instance = Book(title=input.title,
                             year=input.year,
                             author=author)
        book_instance.save()
        return CreateBook(ok=ok, book=book_instance)


class UpdateBook(graphene.Mutation):
    """
        Mutation to update a book with new information
    """
    class Arguments:
        """
            Arguments for mutation method input
        """
        id = graphene.Int(required=True)
        input = BookInput(required=True)

    ok = graphene.Boolean()
    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, id, input=None):
        """
            Mutate method to update a book,
            validates author included in update
        """
        ok = False
        book_instance = Book.objects.get(pk=id)
        if book_instance:
            ok = True
            author = Author.get(pk=input.author.id)
            # author included in update not in authors
            if author is None:
                return UpdateBook(ok=False, book=None)
            book_instance.author = author
            book_instance.title = input.title
            book_instance.year = input.year
            book_instance.save()
            return UpdateBook(ok=ok, book=book_instance)
        return UpdateBook(ok=ok, book=None)


class Mutation(graphene.ObjectType):
    """
        Our set of mutations allowed
    """
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()


# map the queries and the mutations to a schema
schema = graphene.Schema(query=Query, mutation=Mutation)
