import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from backend.synth_app.models import Author, Book


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
        id kwargs.get('id')

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
