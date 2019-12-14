from django import forms
from blog_app.models import *


class TagsForm(forms.ModelForm):
    """Form definition for Tags."""

    class Meta:
        """Meta definition for Tagsform."""

        model = Tags
        fields = ('name',)


class CategoryForm(forms.ModelForm):
    """Form definition for Category."""

    class Meta:
        """Meta definition for Categoryform."""

        model = Category
        fields = ('name', 'description', 'is_active', 'user',)


class PostForm(forms.ModelForm):
    """Form definition for Post."""

    class Meta:
        """Meta definition for Postform."""

        model = Post
        fields = ('title', 'user', 'content', 'category',
                  'tags', 'status', 'keywords', 'featured_image')
