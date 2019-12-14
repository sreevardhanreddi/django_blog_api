from django.shortcuts import HttpResponse, render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from blog_app.models import *
from blog_app.serializers import *

# Create your views here.


def index(request):
    return HttpResponse('something')


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def blog_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    blog_posts = Post.objects.all()
    paginated_results = paginator.paginate_queryset(blog_posts, request)
    serializer = BlogPostSerializer(paginated_results, many=True)
    return paginator.get_paginated_response(serializer.data)


class TagCreate(ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny, ]


class CategoryCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]
