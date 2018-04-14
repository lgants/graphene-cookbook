import graphene

import cookbook.ingredients.schema


class Query(cookbook.ingredients.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries as more apps added to the project
    pass

schema = graphene.Schema(query=Query)
