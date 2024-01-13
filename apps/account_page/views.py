from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.urls import reverse

from apps.account_page.models import AccountTestProgress, Profile
from apps.account_page.forms import (
    AccountTestProgressForm,
    CURRENT_STATUS_CODES,
    FINAL_STATUS_CODES,
)
from apps.test_progress.models import TestObject, Question, Answer
from apps.main.scripts import register_user_activity


from misc.template_styling_components import show_test_card


# @register_user_activity
@login_required()
def view_account_page(request):

    context = {"tests_list": []}
    res = []

    user_profile = Profile.objects.get(user_id=request.user.pk)

    for test_progress in AccountTestProgress.objects.filter(profile=user_profile.pk):

        res.append(
            show_test_card(
                test=test_progress.tests.first(),
                test_progress=test_progress,
            )
        )

    context["tests_list"] = mark_safe(
        '<div style="margin-top:45px; display: inline-block; width: 100%;">'
        + "".join(res)
        + "</div>"
    )

    return render(request, "account_page.html", context)


@login_required()
def test_description(request, pk):
    """Render test_description.html file"""

    test_progress = AccountTestProgress.objects.get(pk=pk)
    profile = test_progress.profile.first()
    test = test_progress.tests.first()

    question_list = Question.objects.filter(test_object=test)

    # view finished trsst attempt
    questions_answers = []
    if test_progress.current_status not in (0, 1):
        for checked_question, checked_answer in test_progress.result_detailed.get(
            "answers"
        ).items():

            question = Question.objects.filter(pk=checked_question).first()
            answer = Answer.objects.filter(pk=checked_answer).first()

            questions_answers.append(
                (
                    (question.question, question.marks),
                    (answer.answer, answer.is_correct),
                )
            )

    request.session["answers"] = {}

    context = {
        "test": test,
        "editable": test_progress.current_status in (0, 1),
        "test_progress": test_progress,
        "questions_answers": questions_answers,
        "first_question_id": question_list[0].pk,
        "test_question_amount": len(question_list),
    }
    return render(request, "test_description.html", context)


@login_required()
def question_details(request, pk, question_pk):
    """Render question_details.html file. Show questions with answers one by one on separate page"""
    try:

        test_progress = AccountTestProgress.objects.get(pk=pk)
        profile = test_progress.profile.first()
        test = test_progress.tests.first()

        question_list = Question.objects.filter(test_object=test)
        question_pk_list = [question.pk for question in question_list]
        current_question_index = question_pk_list.index(question_pk)

        if current_question_index == len(question_list) - 1:
            last_question = True
            next_question_id = question_list[question_pk_list.index(question_pk)]
        else:
            last_question = False
            next_question_id = question_list[question_pk_list.index(question_pk) + 1]

        question = get_object_or_404(Question, pk=question_pk)
        answers = Answer.objects.filter(question=question).order_by("?")

        context = {
            "test": test,
            "question": question,
            "test_progress": test_progress,
            "answers": answers,
            "next_question_id": next_question_id,
            "last_question": last_question,
            "current_question_number": question_pk_list.index(question_pk) + 1,
            "test_question_amount": len(question_list),
        }

        if request.method == "POST":

            print(f'before adding {request.session["answers"]=}', file=sys.stdout)

            if "last" not in request.POST:

                checked_answers_pk_list = request.POST.getlist("radio")
                answers_dict = request.session.get("answers", {})
                answers_dict.update(
                    {
                        str(
                            question_pk_list[question_pk_list.index(question_pk) - 1]
                        ): checked_answers_pk_list
                    }
                )

                request.session["answers"] = answers_dict

                print(f'after adding {request.session["answers"]=}', file=sys.stdout)

            if "last" in request.POST:

                checked_answers_pk_list = request.POST.getlist("radio")
                answers_dict = request.session.get("answers", {})
                answers_dict.update(
                    {str(question_pk_list[-1]): checked_answers_pk_list}
                )

                print(f'after adding {request.session["answers"]=}', file=sys.stdout)

                total_points = 0

                for checked_questions, checked_answers_pk_list in request.session[
                    "answers"
                ].items():
                    for checked_answer_pk in checked_answers_pk_list:

                        if (
                            Answer.objects.filter(pk=checked_answer_pk)
                            .first()
                            .is_correct
                        ):

                            total_points += (
                                Question.objects.filter(pk=checked_questions)
                                .first()
                                .marks
                            )

                test_progress.result_detailed = {
                    "total_points": total_points,
                    "answers": request.session["answers"],
                }

                test_progress.result = total_points

                test_progress.save()

                return redirect(view_account_page)
            else:
                return render(request, "question_details.html", context)
        else:
            return render(request, "question_details.html", context)

    except Exception as e:
        raise e


def view_tests_passing(request, pk):

    test_progress = AccountTestProgress.objects.get(pk=pk)
    profile = test_progress.profile.first()

    test = test_progress.tests.first()

    questions_answers = {}
    for question in list(Question.objects.filter(test_object=test)):
        questions_answers.update({(question.pk, question.question, question.marks): []})

        for answer in Answer.objects.filter(question=question).order_by("?"):
            questions_answers.get(
                (question.pk, question.question, question.marks)
            ).append((answer.pk, answer.answer))

    context = {
        "test": test,
        "profile": profile,
        "test_progress_pk": test_progress.pk,
        "questions_answers": questions_answers,
    }

    if request.method == "POST":

        id_list = request.POST.getlist("checkbox")
        # checked_answers = [Answer.objects.get(pk=int(answer_id)) for answer_id in id_list]

        # correct = all([answer.is_correct for answer in checked_answers])
        # unchecked_answers = [answer.is_correct for answer in answers if answer not in checked_answers]

        # if 'submit' in request.POST or True:
        context = {
            "id_list": id_list,
            # "checked_answers": checked_answers,
        }

        # return render(request, "tt.html", context)

    return render(request, "test_passing.html", context)
