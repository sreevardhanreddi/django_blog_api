from django.urls import path
from blog_app.views import *

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('blogs/', blog_list, name='blog_list'),
    path('tag/create/', TagCreate.as_view(), name='tag_create'),
    path('category/create/', CategoryCreate.as_view(), name='category_create'),


]
