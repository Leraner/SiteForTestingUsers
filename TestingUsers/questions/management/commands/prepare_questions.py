from django.core.management.base import BaseCommand, CommandError

from questions.models import Question


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(20):
            Question.objects.create(question_text=f'TestText{i}')
            print(f'TestText{i} created')

        print('All questions has been created')

