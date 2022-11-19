from rest_framework.routers import SimpleRouter

from questions.views import QuestionView

router = SimpleRouter()

router.register('', QuestionView, basename='question')

urlpatterns = []

urlpatterns += router.urls
