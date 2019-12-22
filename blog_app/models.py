from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Tags'
        verbose_name_plural = 'Tags'
        ordering = ('id',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tags, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('id',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug


STATUS_CHOICE = (
    ('Draft', 'Draft'),
    ('Publish', 'Publish'),
    ('Reject', 'Reject'),
    ('Trash', 'Trash'),
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    # meta_description = models.TextField(max_length=160, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=None, null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, related_name='rel_posts')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICE, default='Draft')
    keywords = models.TextField(max_length=500, blank=True)
    featured_image = models.ImageField(
        upload_to='uploads/blog_cover_image/', blank=True, null=True,
        default='/default/blogging.png')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ('id',)
