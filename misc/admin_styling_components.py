from django.utils.safestring import mark_safe

from django.urls import reverse

from apps.test_progress.models import Answer
from misc.admin_supprotive_blocks import (
    show_data_colored_border_block,
    show_data_colored_badge,
)

from apps.account_page.forms import CURRENT_STATUS_CODES


def show_article(article):

    return show_data_colored_border_block(
        text=article.title,
        text_bold=False,
        color="yellow",
        link_href=reverse("admin:articles_article_change", args=[article.pk]),
        extra_styles="width:300px;",
    )


def show_user_profile_card(
    profile,
):

    text = f"""
    <div style="font-size:18px;margin-bottom:auto;margin-top:0px">{profile.user.email}</div>
    <div style="font-size:14px;margin-bottom:0px;margin-top:auto">{profile.user.first_name} {profile.user.last_name}</div>
    """

    # _ = ''

    link_text = f"""<a href="{reverse("admin:account_page_profile_change", args=[profile.pk])}" 
        style="color:white;padding:0px; height:52px;display: grid;">"""

    if profile.is_admin:
        profile_type_style = "border-left:5px solid tomato;"
    else:
        profile_type_style = "border-left:5px solid blue;"

    return mark_safe(
        f"""<div style="background-color: #353535;display: flex;
        padding: 5px;margin-bottom:5px;margin-right:5px;width:250px;
        line-height: 1;text-align: left;min-width:50px;{profile_type_style}
        vertical-align: baseline;border-radius:5px;font-size: 12px;">
        {link_text}{text}</a></div>"""
    )


def show_linker_block(
    linker,
):
    return mark_safe(
        f"""
            <a href="{reverse("admin:account_page_accounttestprogress_change", args=[linker.pk])}">
                <div style="display:flex;">                    
                    <div style="width:190px;background:#353535;text-align: left;font-size: 15px;
                    text-align: left;align-items: center;padding:10px;
                    border-radius:5px;color: white;">
                        <div style="margin-bottom:10px;display:flex;">
                            <div style="margin-right: auto;">Результат:</div>
                            <div>{linker.result}</div>
                        </div>
                        <div style="margin-top:10px;display:flex;">
                            <div style="margin-right: auto;">Статус:</div> 
                            <div>{dict(CURRENT_STATUS_CODES).get(str(linker.current_status))}</div>
                        </div>
                    </div>
                </div>        
            </a>
            """
    )


def show_popular_block(
    popular_element,
):
    enabled_text, enabled_color = (
        ("Да", "green") if popular_element.enabled else ("Нет", "red")
    )

    return mark_safe(
        f"""
            <a href="{reverse("admin:popular_element_populararticle_change", args=[popular_element.pk])}">
                <div style="display:flex;font-weight: normal;">                  
                    <div style="width:190px;background:#353535;text-align: left;font-size: 15px;
                    text-align: left;align-items: center;padding:3px 10px 3px 10px;
                    border-radius:5px;color: white;">
                        <div style="display:flex;font-weight: bold;font-size:16px">
                            <div style="margin-right: auto;">{popular_element.title}</div>
                        </div>
                        <div style="margin-top:15px;display:flex;">
                            <div style="margin-right: auto;">Число статей:</div> 
                            <div>{str(len(popular_element.articles.all()))}</div>
                        </div>
                        <div style="margin-top:8px;display:flex;">
                            <div style="margin-right: auto;">Включено:</div> 
                            <div>{show_data_colored_badge(color=enabled_color, text=enabled_text, text_bold=True)}</div>
                        </div>
                    </div>
                </div>
            </a>
            """
    )


def show_categories_tiles_block(
    categories_tiles_element,
):
    enabled_text, enabled_color = (
        ("Да", "green") if categories_tiles_element.enabled else ("Нет", "red")
    )

    return mark_safe(
        f"""
            <a href="{reverse("admin:popular_element_categoriestiles_change", args=[categories_tiles_element.pk])}">
                <div style="display:flex;font-weight: normal;">                  
                    <div style="width:190px;background:#353535;text-align: left;font-size: 15px;
                    text-align: left;align-items: center;padding:3px 10px 3px 10px;
                    border-radius:5px;color: white;">
                        <div style="display:flex;font-weight: bold;font-size:16px">
                            <div style="margin-right: auto;">{categories_tiles_element.title}</div>
                        </div>
                        <div style="margin-top:15px;display:flex;">
                            <div style="margin-right: auto;">Число категорий:</div> 
                            <div>{str(len(categories_tiles_element.categories.all()))}</div>
                        </div>
                        <div style="margin-top:8px;display:flex;">
                            <div style="margin-right: auto;">Включено:</div> 
                            <div>{show_data_colored_badge(color=enabled_color, text=enabled_text, text_bold=True)}</div>
                        </div>
                    </div>
                </div>
            </a>
            """
    )


def show_test_block(test):
    return show_data_colored_border_block(
        text=test.test_object_name,
        text_bold=False,
        color="aquamarine",
        link_href=reverse("admin:test_progress_testobject_change", args=[test.pk]),
    )


def show_question_block(question):
    return show_data_colored_border_block(
        text=question.question,
        color="yellow",
        link_href=reverse("admin:test_progress_question_change", args=[question.pk]),
    )


def show_answer_block(
    question_object,
):
    return show_data_colored_border_block(
        text=question_object.question,
        color="yellow",
        link_href=reverse(
            "admin:test_progress_question_change", args=[question_object.pk]
        ),
    )


def show_answer_block_quiestions(question_object):

    text = question_object.question
    color = "yellow"

    link_text = f"""
    <a href="{reverse("admin:test_progress_question_change", args=[question_object.pk])}" 
        style="color:white;font-size:16px;padding:0px;display: flex;">"""

    answers = []
    for i, answer in enumerate(list(Answer.objects.filter(question=question_object))):
        answers.append(
            show_data_colored_badge(
                text=answer.answer,
                text_bold=False,
                color="green" if answer.is_correct else "red",
                extra_styles="text-align: left;",
            )
        )

    answers_block = (
        arange_block_box(
            elements=answers, min_width=150, custom_styles="margin-top:10px;"
        )
        if answers
        else ""
    )

    return mark_safe(
        f"""<div style="background-color: #353535;display: grid; width: fit-content;
        padding:5px;font-size: 12px;margin-bottom:6px;margin-right:5px;
        line-height: 1;text-align: left;border-left:5px solid {color};
        vertical-align: baseline;border-radius:5px;font-size: 16px;">
        {link_text}<div>{text}</div>
        <div style="margin-right: 0px;margin-left: auto; text-align: end;font-size:14px;">
        {question_object.marks} балл(а)</div></a>
        {answers_block}</div>"""
    )


def arange_block_box(elements, min_width=None, max_width=None, custom_styles=""):
    return mark_safe(
        f"""<div style="display:inline-grid;
        {f'min-width:{min_width}px;' if min_width else ''}
        {f'max-width:{max_width}px;' if max_width else ''}
        {custom_styles}">
        {''.join(elements)}
        </div>
        """
    )
