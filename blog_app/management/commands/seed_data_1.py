import json
from django.core.management.base import BaseCommand
from blog_app.models import *


class Command(BaseCommand):
    help = 'seeds data to db'

    def handle(self, *args, **kwargs):
        print('seeding data ...')
        with open('seed_data/tags.json') as f:
            json_data = json.load(f)
            for data in json_data:
                Tags.objects.create(name=data.get('name'), slug=data.get('slug'))

        with open('seed_data/categories.json') as f:
            json_data = json.load(f)
            for data in json_data:
                Category.objects.create(name=data.get(
                    'name'), description=data.get('description'))

        with open('seed_data/posts.json') as f:
            json_data = json.load(f)
            for data in json_data:
                post = Post.objects.create(
                    title=data.get('title'),
                    content=data.get('content'),
                    category_id=data.get('category').get('id'),
                )
                tags = data.get('tags')
                for tag in tags:
                    post.tags.add(tag.get('id'))

        print('Finished seeding data !!!')
