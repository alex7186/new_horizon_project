from django.contrib import admin
from apps.test_progress.models import Test

from django.utils.safestring import mark_safe


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    def show_test_card(self, obj):

        if obj.type == 1:
            type_text = "Процентный результат"
        elif obj.type == 2:
            type_text = "Пройдено / Не пройдено"

        text = f"""
            <div style="width:250px;>
                <div style="">#{obj.pk} {obj.header_text}</div>
                <div style="font-size:10px;margin-top:5px;">{obj.detailed_text}</div>
                <div style="margin-top:15px;">{type_text}</div>
            </div>
            """

        return mark_safe(
            f"""<div style="background-color: #353535;width:350px;
            color:white;font-size:14px!important;padding:0px;display: inline-block;
            padding: 5px;font-size: 75%;font-weight: 700; margin-bottom:10px;
            line-height: 1;text-align: left;min-width:50px;border-left:5px solid yellow;
            border-radius: .25rem;font-size: 12px;display: flow-root;">
            {text}</div>
            """
        )

    show_test_card.short_description = "Карточка теста"

    def show_test_type(self, obj):

        if obj.type == 1:
            type_text = "Процентный результат"
        elif obj.type == 2:
            type_text = "Пройдено / Не пройдено"

        return mark_safe(
            f"""
            <div style="background-color: #353535;display: inline-block;
                padding:5px;font-size: 75%;margin-bottom:5px;
                line-height: 1;text-align: left;width: 160px;
                vertical-align: baseline;border-radius:5px;font-size: 16px;">
                    <div style="font-size: 14px;">#{obj.type}</div>
                    <div style="font-size: 14px;margin-top: 10px;">{type_text}</div>
                    
                </div>
            </div>
            """
        )

    show_test_type.short_description = "Тип теста"

    list_display = (
        "show_test_card",
        # "show_test_type",
    )
