from rest_framework.routers import SimpleRouter

from answers.views import AnswerView

router = SimpleRouter()

router.register('', AnswerView, basename='answers')

urlpatterns = []

urlpatterns += router.urls
