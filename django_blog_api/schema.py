import graphene

import blog_app.schema
import common.schema


class Query(common.schema.Query, blog_app.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)