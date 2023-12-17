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
    def show_test(self):

        return show_test_block(
            test=TestObject.objects.filter(test_object_name=self.test_object).first()
        )

    show_test.short_description = "Название теста 👇"

    def show_questions(self):

        return show_answer_block_quiestions(self)

    show_questions.short_description = "Вопросы 👇"

    list_display = (
        show_test,
        show_questions,
    )

    inlines = (AnswerInlineAdmin,)


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

            res.append(
                show_answer_block_quiestions(question_object)
                # show_answer_block(question_object)
            )

        return arange_block_box(res)
        # return mark_safe(res)

    show_questions.short_description = "Вопросы 👇"

    form = TestObjectForm

    list_display = (
        show_test,
        show_questions,
    )

    inlines = (QuestionInlineAdmin,)

    # list_filter = (
    #     "test_object_name",
    # )

    # readonly_fields = ('test_object_name',)
