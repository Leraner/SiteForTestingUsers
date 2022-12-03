from django.contrib import admin
from .models import Exam, ExamQuestion, ExamAnswer

admin.site.register(Exam)
admin.site.register(ExamQuestion)
admin.site.register(ExamAnswer)
