import arrow
import graphene
from graphene_django.types import DjangoObjectType

from blog_app.models import Category, Post, Tags


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class TagType(DjangoObjectType):
    class Meta:
        model = Tags


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        convert_choices_to_enum = False
        # convert_choices_to_enum this is used to get choices as text
        # fields= ('id', 'title')
        # you can also specify what fields to include

    arrow_created_on = graphene.String()

    def resolve_arrow_created_on(self, info):
        return arrow.get(self.created_on).humanize()


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_tags = graphene.List(TagType)
    all_posts = graphene.List(PostType)
    category = graphene.Field(CategoryType, category_id=graphene.String())
    blog_post_first = graphene.Field(
        PostType, post_content_search=graphene.String())
    blog_post_all = graphene.List(
        PostType, post_content_search=graphene.String())

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_category(self, info, category_id):
        return Category.objects.get(id=category_id)

    def resolve_all_tags(self, info, **kwargs):
        return Tags.objects.all()

    def resolve_all_posts(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        """ return # Post.objects.select_related('category').all() # """
        return Post.objects.all()

    def resolve_blog_post_first(self, info, post_content_search):
        return Post.objects.filter(content__icontains=post_content_search).first()

    def resolve_blog_post_all(self, info, post_content_search):
        return Post.objects.filter(content__icontains=post_content_search).all()
