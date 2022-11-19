import json
from random import sample

from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAuthenticatedOrAdminOrReadOnly
from questions.models import Question
from questions.serializer import QuestionSerializer


class TestingUsersPagination(PageNumberPagination):
    """Pagination class for site"""
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100


class QuestionView(ModelViewSet):
    """Exercise view"""
    serializer_class = QuestionSerializer
    pagination_class = TestingUsersPagination
    permission_class = IsAuthenticatedOrAdminOrReadOnly

    def get_queryset(self):
        return Question.objects.all()

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def question_list(self, request):
        if int(request.data['questions_count']) > Question.objects.count():
            return Response({"data": "There are not so many questions"})

        queryset = sample(list(Question.objects.all()),
                          k=int(request.data['questions_count']))

        queryset = self.paginate_queryset(queryset)
        serializer = QuestionSerializer(queryset, many=True)
        return Response({'data': json.loads(json.dumps(serializer.data))})
