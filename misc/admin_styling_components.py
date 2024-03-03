from django.utils.safestring import mark_safe

from django.urls import reverse

from apps.test_progress.models import Answer, Question
from misc.admin_supprotive_blocks import (
    show_data_colored_border_block,
    show_data_colored_badge,
)

from apps.test_progress.forms import CURRENT_STATUS_CODES, TEST_TYPES_CODES


def show_article(article):

    return show_data_colored_border_block(
        text=article.title,
        text_bold=False,
        color="yellow",
        link_href=reverse("admin:articles_article_change", args=[article.pk]),
        extra_styles="width:300px;font-weight: normal;font-size:10px !important;",
    )


def show_user_profile_card(
    profile,
):

    text = f"""
    <div style="font-size:10px;margin-bottom:auto;margin-top:0px">{profile.user.email}</div>
    <div style="font-size:10px;margin-bottom:0px;margin-top:auto">{profile.user.first_name} {profile.user.last_name}</div>
    """

    # _ = ''

    link_text = f"""<a href="{reverse("admin:account_page_profile_change", args=[profile.pk])}" 
        style="color:white;padding:0px; height:30px;display: grid;">"""

    if profile.is_admin:
        profile_type_style = "border-left:5px solid tomato;"
    else:
        profile_type_style = "border-left:5px solid blue;"

    return mark_safe(
        f"""<div style="background-color: #353535;display: flex;
        padding: 5px;margin-bottom:5px;margin-right:5px;width:250px;
        line-height: 1;text-align: left;min-width:50px;{profile_type_style}
        vertical-align: baseline;border-radius:5px;font-size: 10px;font-weight: normal;">
        {link_text}{text}</a></div>"""
    )


def show_linker_block(
    linker,
):
    return mark_safe(
        f"""
            <a href="{reverse("admin:test_progress_accounttestprogress_change", args=[linker.pk])}">
                <div style="display:flex;">                    
                    <div style="width:190px;background:#353535;text-align: left;font-size: 10px;
                    text-align: left;align-items: center;padding: 5px;
                    border-radius:5px;color: white;">
                        <div style="display:flex;">
                            <div style="margin-right: auto;">Результат:</div>
                            <div>{linker.result}</div>
                        </div>
                        <div style="margin-top:6px;display:flex;">
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
    count,
):
    enabled_text, enabled_color = (
        ("Да", "green") if popular_element.enabled else ("Нет", "red")
    )

    return mark_safe(
        f"""
            <a href="{reverse("admin:popular_element_populararticle_change", args=[popular_element.pk])}">
                <div style="display:flex;font-weight: normal;">                  
                    <div style="width:190px;background:#353535;text-align: left;font-size: 10px;
                    text-align: left;align-items: center;padding:3px 10px 3px 10px;
                    border-radius:5px;color: white;">
                        <div style="display:flex;font-weight: normal;font-size:14px;margin-top:6px">
                            <div style="margin-right: auto;">{popular_element.title}</div>
                        </div>
                        <div style="margin-top:6px;display:flex;">
                            <div style="margin-right: auto;">Число статей:</div> 
                            <div>{count}</div>
                        </div>
                        <div style="display:flex;">
                            <div style="margin-right: auto;">Включено:</div> 
                            <div>{show_data_colored_badge(color=enabled_color, text=enabled_text, text_bold=True)}</div>
                        </div>
                    </div>
                </div>
            </a>
            """
    )


def show_load_excel_block(load_element, show_link=True):

    link_text = f'<a href="/static/{load_element.stored_file}">' if show_link else ""

    return mark_safe(
        f"""
            
                <div style="display:flex;font-weight: normal;">                  
                    <div style="width:290px;background:#353535;text-align: left;font-size: 15px;
                    text-align: left;align-items: center;padding:6px 10px 6px 10px;
                    border-radius:5px;color: white;">
                        <div style="display:flex;">
                            <div style="margin-right: auto;">Файл:</div> 
                            <div>
                                {link_text}{load_element.stored_file}{'</a>' if link_text else ''}
                            </div>
                        </div>
                        <div style="margin-top:8px;display:flex;">
                            <div style="margin-right: auto;">Дата формирования выгрузки:</div> 
                            <div>{load_element.last_used_at.strftime("%Y.%m.%d %H:%M")}</div>
                        </div>
                    </div>
                </div>
            
            """
    )


def show_test_block(test):

    text = f"""
    <div style="font-size:12px;margin-bottom:auto;margin-top:0px;
    margin-bottom:10px;">{test.test_object_name}</div>

    
    <div style="margin-bottom:4px;display:flex;">
        <div style="margin-right: auto;">Тип:</div>
        <div>{dict(TEST_TYPES_CODES)[test.test_type]}</div>
    </div>
    
    <div style="margin-bottom:4px;display:flex;">
        <div style="margin-right: auto;">Результат:</div>
        <div>12</div>
    </div>
    <div style="margin-bottom:2px;display:flex;">
        <div style="margin-right: auto;">Число вопросов:</div>
        <div>{len(Question.objects.filter(test_object=test.pk))}</div>
    </div>
    """

    # _ = ''

    link_text = f"""<a href="{reverse("admin:test_progress_testobject_change", args=[test.pk])}" 
        style="color:white;padding:0px;display:grid;width: 100% !important;">"""

    return mark_safe(
        f"""<div style="background-color: #353535;display: flex;
        padding: 5px;width:250px;
        line-height: 1;text-align: left;border-left:5px solid aquamarine;
        vertical-align: baseline;border-radius:5px;font-size: 10px !important;font-weight:normal;">
        {link_text}{text}</a></div>"""
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
        style="color:white;font-size:12px;padding:3px 6px 3px 6px;display: flex;">"""

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
        padding:5px;font-size: 12px !important;margin-bottom:6px;margin-right:5px;
        line-height: 1;text-align: left;border-left:5px solid {color};
        vertical-align: baseline;border-radius:5px;font-weight:normal;">
        {link_text}<div>{text}</div>
        <div style="margin-right: 0px;margin-left: auto; text-align: end;font-size:10px;">
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
