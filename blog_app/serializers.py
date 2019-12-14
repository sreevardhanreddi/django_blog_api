from blog_app.models import *
from rest_framework import serializers
from common.serializers import *


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ['name', 'slug', 'id']


class CategorySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'is_active', 'user', 'id']


class BlogPostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    tags = TagSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['title', 'slug', 'created_on', 'updated_on', 'user', 'content',
                  'category', 'tags', 'status', 'keywords', 'featured_image', ]
