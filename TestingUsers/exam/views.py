from answers.exceptions import DataNotFoundException, UserNotFoundException
from django_filters.rest_framework import DjangoFilterBackend
from post.permissions import IsAuthOrReadOnly
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Exam, ExamAnswer, ExamQuestion
from .serializer import (ExamAnswerSerializer, ExamQuestionSerializer,
                         ExamSerializer)
from .services import ExamConductor, ExaminationTest


# TODO: Do tests with exam pagination, create 11 exams and test it
# TODO: Create logic to exam's page


class ExamPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "exam_question_len"
    max_page_size = 10


class ExamAnswerView(ExaminationTest, ModelViewSet):
    serializer_class = ExamAnswerSerializer
    pagination_class = ExamPagination
    permission_class = IsAuthOrReadOnly

    def get_queryset(self):
        return ExamAnswer.objects.all()

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def my_answers_and_questions(self, request):
        queryset = self.get_queryset().filter(author=request.user)
        return self.paginate_answers(queryset)

    def paginate_answers(self, queryset):
        questions_on_page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(questions_on_page, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def checked_list_of_exam_answers(self, request):
        """
        This is case for check answers that come from user's test
        If the user tries to answer not first time, we don't accrue points for that answers
        :request
        {
        notFirstTrt: bool,
        questionsList: [
                {
                    id: int
                    answer_text: str
                },
            ]
        }

        :return
            [
                {
                    question_id: int,
                    answer: str,
                    correct: bool,
                }
            ]
        """
        try:
            response = self._reconciliation_of_answers(request.data.get('questionsList'), request.user.id,
                                                       request.data.pop('notFirstTry', True))
            return Response({"result": response})
        except (UserNotFoundException, DataNotFoundException) as error:
            return Response({"result": {"message": str(error), "status_code": 404}})


class ExamQuestionView(ModelViewSet):
    serializer_class = ExamQuestionSerializer
    pagination_class = ExamPagination
    permission_class = IsAuthOrReadOnly

    def get_queryset(self):
        return ExamQuestion.objects.all()

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def my_questions(self, request):
        queryset = self.get_queryset().filter(author=request.user)
        return self.paginate_questions(queryset)

    def paginate_questions(self, queryset):
        questions_on_page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(questions_on_page, many=True)
        return self.get_paginated_response(serializer.data)


class ExamView(ExamConductor, ModelViewSet):
    serializer_class = ExamSerializer
    filter_backends = [DjangoFilterBackend]
    permission_class = IsAuthOrReadOnly
    pagination_class = ExamPagination

    lookup_field = 'author__username'
    filterset_fields = ['id']

    def get_queryset(self):
        return Exam.objects.all()

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def my_exams(self, request):
        queryset = self.get_queryset().filter(author=request.user)
        serializer = ExamSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def paginate_exams(self, queryset):
        exams_on_page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(exams_on_page, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        response_data = self._create_exam(request.user, request.data)
        return Response(response_data)
