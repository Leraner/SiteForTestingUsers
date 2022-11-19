from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from answers.models import Answer
from answers.serializer import AnswerSerializer
from questions.views import TestingUsersPagination
from .exceptions import UserNotFoundException, DataNotFoundException
from .services import Examination


class AnswerView(Examination, ModelViewSet):
    serializer_class = AnswerSerializer
    pagination_class = TestingUsersPagination
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Answer.objects.all()

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def checked_list_of_answers(self, request):
        """
        This is case for check answers that come
        If the user tries to answer not first time, we don't accrue points for this answers
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
