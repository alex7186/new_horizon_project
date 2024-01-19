from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from apps.test_progress.models import TestObject, Question, Answer
from apps.main.scripts import register_user_activity
from apps.account_page.forms import (
    AccountTestProgressForm,
    CURRENT_STATUS_CODES,
    FINAL_STATUS_CODES,
)


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

    if test_progress.attemp_started == None:
        test_progress.attemp_started = datetime.now()
        test_progress.save()

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

        if "last" not in request.POST:

            checked_answers_pk_list = request.POST.getlist("radio")[0]
            answers_dict = request.session.get("answers", {})
            answers_dict.update(
                {
                    str(
                        question_pk_list[question_pk_list.index(question_pk) - 1]
                    ): checked_answers_pk_list
                }
            )

            request.session["answers"] = answers_dict

        if "last" in request.POST:

            checked_answers_pk_list = request.POST.getlist("radio")[0]
            answers_dict = request.session.get("answers", {})
            answers_dict.update({str(question_pk_list[-1]): checked_answers_pk_list})

            total_points = 0

            for checked_questions, checked_answer_pk in request.session[
                "answers"
            ].items():

                if Answer.objects.filter(pk=checked_answer_pk).first().is_correct:

                    total_points += (
                        Question.objects.filter(pk=checked_questions).first().marks
                    )

            test_progress.result_detailed = {
                "total_points": total_points,
                "answers": request.session["answers"],
            }
            test_progress.attemp_finished = datetime.now()
            test_progress.result = total_points

            test_progress.save()

            return redirect(view_account_page)
        else:
            return render(request, "question_details.html", context)
    else:
        return render(request, "question_details.html", context)
