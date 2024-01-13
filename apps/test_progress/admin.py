from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.test_progress.models import Question, Answer, TestObject
from apps.test_progress.forms import TestObjectForm

from misc.admin_supprotive_blocks import show_data_colored_border_block
from misc.admin_styling_components import (
    show_test_block,
    show_question_block,
    arange_block_box,
    show_answer_block,
    show_answer_block_quiestions,
)


class AnswerInlineAdmin(admin.StackedInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

    def show_test(self):

        return show_test_block(
            test=TestObject.objects.get(test_object_name=self.test_object)
        )

    show_test.short_description = "Название теста 👇"

    def show_questions(self):

        return arange_block_box(
            show_answer_block_quiestions(self),
        )

    show_questions.short_description = "Вопросы 👇"

    list_display = (
        show_questions,
        # show_test,
    )

    inlines = (AnswerInlineAdmin,)

    list_filter = ("test_object__test_object_name",)


class QuestionInlineAdmin(admin.StackedInline):
    model = Question


@admin.register(TestObject)
class TestObjectAdmin(admin.ModelAdmin):
    def show_test(self):

        return show_test_block(test=self)

    show_test.short_description = "Название теста 👇"

    def show_questions(self):

        res = []
        for question_object in list(Question.objects.filter(test_object=self)):

            res.append(show_answer_block_quiestions(question_object))

        return arange_block_box(res)

    show_questions.short_description = "Вопросы 👇"

    form = TestObjectForm

    list_display = (
        show_test,
        show_questions,
    )

    inlines = (QuestionInlineAdmin,)

    list_filter = ("test_object_name",)
