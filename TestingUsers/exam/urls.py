from rest_framework.routers import SimpleRouter

from .views import ExamView, ExamQuestionView, ExamAnswerView

router = SimpleRouter()

router.register('exam_answers', ExamAnswerView, basename='exam_answers')
router.register('exam_questions', ExamQuestionView, basename='exam_questions')
router.register('exam', ExamView, basename='exam')

urlpatterns = []

urlpatterns += router.urls
