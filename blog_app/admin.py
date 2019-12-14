from django.contrib import admin
from blog_app.forms import *
from blog_app.models import *
# Register your models here.


class TagsAdmin(admin.ModelAdmin):
    form = TagsForm
    # you can also the customize the form fields 
    # for admin here by creating another 
    # model form specifically for admin


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm


class PostAdmin(admin.ModelAdmin):
    form = PostForm


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
