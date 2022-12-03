from django.core.management.base import BaseCommand
from post.models import Category
from users.models import CustomUser


class Command(BaseCommand):
    CATEGORIES = {'other': 'Other'}

    def handle(self, *args, **options):
        admin = CustomUser.objects.filter(username='admin').first()
        if admin is None:
            CustomUser.objects.create_superuser(username='admin', password='admin')
        print(f'Admin has been created')

        for category in self.CATEGORIES:
            if Category.objects.filter(slug=category).first() is None:
                Category.objects.create(slug=category, title=self.CATEGORIES[category])
            print(f'Category {category} has been created')
