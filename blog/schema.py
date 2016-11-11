import graphene
from graphene_django import DjangoObjectType
from blog.models import Blog as BlogModel


class Blog(DjangoObjectType):
    class Meta:
        model = BlogModel


class Query(graphene.ObjectType):
    blog = graphene.List(Blog)

    @graphene.resolve_only_args
    def resolve_users(self):
        return Blog.objects.all()


schema = graphene.Schema(query=Query)
