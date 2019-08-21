import graphene
import backend.synth_app.schema as schema_import


class Query(schema_import.Query, graphene.ObjectType):
    """
        This class will inherit from  multiple Queries
        as we add more apps to the project

        Allowing us to have multiple apps rather than
        one huge schema file for graphql and all apps

        Essentially a method of decoupling
    """
    pass


class Mutation(schema_import.Mutation, graphene.ObjectType):
    """
        This class will inherit from  multiple Mutations
        as we add more apps to the project

        Allowing us to have multiple apps rather than
        one huge schema file for graphql and all apps

        Essentially a method of decoupling
    """
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
