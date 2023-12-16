from django.contrib import admin

from apps.test_progress.models import Question, Answer, TestObject

from django.utils.safestring import mark_safe

from misc.admin_styling_components import (
    show_data_colored_border_block,
    show_data_colored_badge,
    arange_block_box,
)

# @admin.register(Test)
# class TestAdmin(admin.ModelAdmin):
#     def show_test_card(self, obj):

#         if obj.type == 1:
#             type_text = "Процентный результат"
#         elif obj.type == 2:
#             type_text = "Пройдено / Не пройдено"

#         text = f"""
#             <div style="width:250px;>
#                 <div style="">#{obj.pk} {obj.header_text}</div>
#                 <div style="font-size:10px;margin-top:5px;">{obj.detailed_text}</div>
#                 <div style="margin-top:15px;">{type_text}</div>
#             </div>
#             """

#         return mark_safe(
#             f"""<div style="background-color: #353535;width:350px;
#             color:white;font-size:14px!important;padding:0px;display: inline-block;
#             padding: 5px;font-size: 75%;font-weight: 700; margin-bottom:10px;
#             line-height: 1;text-align: left;min-width:50px;border-left:5px solid yellow;
#             border-radius: .25rem;font-size: 12px;display: flow-root;">
#             {text}</div>
#             """
#         )

#     show_test_card.short_description = "Карточка теста"

#     def show_test_type(self, obj):

#         if obj.type == 1:
#             type_text = "Процентный результат"
#         elif obj.type == 2:
#             type_text = "Пройдено / Не пройдено"

#         return mark_safe(
#             f"""
#             <div style="background-color: #353535;display: inline-block;
#                 padding:5px;font-size: 75%;margin-bottom:5px;
#                 line-height: 1;text-align: left;width: 160px;
#                 vertical-align: baseline;border-radius:5px;font-size: 16px;">
#                     <div style="font-size: 14px;">#{obj.type}</div>
#                     <div style="font-size: 14px;margin-top: 10px;">{type_text}</div>

#                 </div>
#             </div>
#             """
#         )

#     show_test_type.short_description = "Тип теста"

#     list_display = (
#         "show_test_card",
#         # "show_test_type",
#     )


class AnswerInlineAdmin(admin.StackedInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    def show_test(self):

        test_object = list(
            TestObject.objects.filter(test_object_name=self.test_object)
        )[0]

        return show_data_colored_border_block(
            text=test_object.test_object_name,
            text_bold=True,
            color="yellow",
            link_href=f"/admin/test_progress/testobject/{self.pk}/change/",
        )

    show_test.short_description = "Название теста 👇"

    def show_questions(self):

        return show_data_colored_border_block(
            text=self.question,
            color="yellow",
            link_href=f"/admin/test_progress/question/{self.pk}/change/",
        )

    show_questions.short_description = "Название вопроса 👇"

    def show_answer(self):

        res = []
        for i, answer in enumerate(list(Answer.objects.filter(question=self))):
            res.append(
                show_data_colored_badge(
                    text=str(i + 1) + ". " + answer.answer,
                    text_bold=False,
                    color="green" if answer.is_correct else "red",
                    # link_href=f"/admin/test_progress/testobject/{self.pk}/change/",
                )
            )

        return arange_block_box(elements=res, min_width=150)

    show_answer.short_description = "Вариант"

    list_display = (
        show_test,
        show_questions,
        show_answer,
        # show_questions_count,
    )

    inlines = (AnswerInlineAdmin,)


class QuestionInlineAdmin(admin.StackedInline):
    model = Question


@admin.register(TestObject)
class TestObjectAdmin(admin.ModelAdmin):
    def show_test(self):

        return show_data_colored_border_block(
            text=self.test_object_name,
            text_bold=True,
            color="yellow",
            link_href=f"/admin/test_progress/testobject/{self.pk}/change/",
        )

    show_test.short_description = "Название теста 👇"

    def show_questions_count(self):

        res = []
        for question_object in list(Question.objects.filter(test_object=self)):
            text = f"""
            {question_object.question}
            ({len(list(Answer.objects.filter(question=question_object)))} ответ)
            """

            res.append(
                show_data_colored_border_block(
                    text=text,
                    color="yellow",
                    link_href=f"/admin/test_progress/question/{question_object.pk}/change/",
                )
            )

        return mark_safe("<br>".join(res))

    show_questions_count.short_description = "Вопросы"

    list_display = (
        show_test,
        show_questions_count,
    )

    inlines = (QuestionInlineAdmin,)

    # readonly_fields = ('test_object_name',)
