from django.core.management.base import BaseCommand, CommandError
from answers.models import Answer
from questions.models import Question


class Command(BaseCommand):
    def handle(self, *args, **options):
        questions = Question.objects.all()

        if questions is None:
            print('First of all, you need create questions')
            return

        for question, i in zip(questions, range(len(questions))):
            Answer.objects.create(answer_text=f'TestAnswer{i}', question=question)
            print(f'TestAnswer{i} created')
        print('All answers has been created')

