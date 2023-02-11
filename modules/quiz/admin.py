from django.contrib import admin
from modules.quiz.models import QuizPick4


# Register your models here.
@admin.register(QuizPick4)
class QuizPick4Admin(admin.ModelAdmin):
    list_display = (
        "question_title",
        "question_main_text",
    )
