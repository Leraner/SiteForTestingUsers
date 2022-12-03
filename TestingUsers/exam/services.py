from answers.services import Examination
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from .models import Exam, ExamAnswer, ExamQuestion
from .serializer import (ExamAnswerSerializer, ExamQuestionSerializer,
                         ExamSerializer)

CustomUser = get_user_model()


# TODO: Add tests for that application


class ExaminationTest(Examination):
    def _get_right_answer(self, answer_id: int):
        right_answer = None
        try:
            right_answer = ExamAnswer.objects.get(question=answer_id)
        except ObjectDoesNotExist:
            self._get_right_answer(answer_id)

        return right_answer


class ExamConductor:
    """Class for conducting exam's opportunities"""

    def _create_question(self, author: CustomUser, data: dict) -> dict:
        data.update({'author': author.id, **data})
        serializer = ExamQuestionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    def _create_answer(self, author: CustomUser, question: dict, data: dict) -> dict:
        data.update({'author': author.id, 'question': question['id'],  **data})
        serializer = ExamAnswerSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    def _prepare_questions_and_answers(self, author: CustomUser, data: dict) -> list:
        questions = []

        for element in data['body']:
            question_data = self._create_question(
                author=author, data=element.get('question'))
            self._create_answer(
                author=author, question=question_data, data=element.get('answer'))

            questions.append(question_data)

        return questions

    def _create_exam(self, author: CustomUser, data: dict) -> dict:
        questions = self._prepare_questions_and_answers(
            author=author, data=data)

        new_exam = Exam.objects.create(title=data.get('title'), author=author)

        for question in questions:
            new_exam.questions.add(ExamQuestion.objects.filter(
                id=question.get('id')).first())

        exam_serializer = ExamSerializer(instance=new_exam)

        return exam_serializer.data
