from django.utils.safestring import mark_safe

from apps.test_progress.models import Answer
from misc.admin_supprotive_blocks import (
    show_data_colored_border_block,
    show_data_colored_badge,
)


def show_user_profile_card(
    user,
):

    text = f"""<div style="font-size: 15px;font-weight: 700;margin-bottom:20px;">{user.email}</div>
    <p style="font-size:12px;margin:0px;padding:0px;">{user.first_name} {user.last_name}</p>"""

    link_text = f"""<a href="/admin/auth/user/{user.pk}/change/" 
        style="color:white;padding:0px;">"""

    return mark_safe(
        f"""<div style="background-color: #353535;display: inline-block;
        padding: 5px;margin-bottom:5px;margin-right:5px;
        line-height: 1;text-align: left;min-width:50px;border-left:5px solid tomato;
        vertical-align: baseline;border-radius: .25rem;font-size: 12px;">
        {link_text}{text}</a></div>"""
    )


def show_linker_block(
    linker,
):
    return mark_safe(
        f"""
            <a href="/admin/account_page/accounttestprogress/{linker.pk}/change/">
            <div style="width:50px;height:50px;background:#353535;font-size: 30px;
            text-align: center;display: table-cell;vertical-align: middle;
            border-radius:10px;">↔️</div></a>
            """
    )


def show_test_block(test):
    return show_data_colored_border_block(
        text=test.test_object_name,
        text_bold=False,
        color="aquamarine",
        link_href=f"/admin/test_progress/testobject/{test.pk}/change/",
    )


def show_question_block(question):
    return show_data_colored_border_block(
        text=question.question,
        color="yellow",
        link_href=f"/admin/test_progress/question/{question.pk}/change/",
    )


def show_answer_block(
    question_object,
):
    return show_data_colored_border_block(
        text=question_object.question,
        color="yellow",
        link_href=f"/admin/test_progress/question/{question_object.pk}/change/",
    )


def show_answer_block_quiestions(question_object):

    text = question_object.question
    color = "yellow"

    link_text = f"""<a href="/admin/test_progress/question/{question_object.pk}/change/" 
        style="color:white;font-size:14px;padding:0px;margin-bottom:20px;">"""

    answers = []
    for i, answer in enumerate(list(Answer.objects.filter(question=question_object))):
        answers.append(
            show_data_colored_badge(
                text=str(i + 1) + ". " + answer.answer,
                text_bold=False,
                color="green" if answer.is_correct else "red",
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
        f"""<div style="background-color: #353535;display: inline-block;
        padding:5px;font-size: 75%;
        margin-bottom:5px;margin-right:5px;
        line-height: 1;text-align: left;min-width:50px;border-left:5px solid {color};
        min-width: 250px; max-width: 400px;
        vertical-align: baseline;border-radius:5px;font-size: 12px;">
        {link_text}{text}{'</a>' if link_text else ''}
        {answers_block}</div>"""
    )


def arange_block_box(elements, min_width=None, max_width=None, custom_styles=""):
    return mark_safe(
        f"""<div style="display:block;
        {f'min-width:{min_width}px;' if min_width else ''}
        {f'max-width:{max_width}px;' if max_width else ''}
        {custom_styles}">
        {''.join(elements)}
        </div>
        """
    )
