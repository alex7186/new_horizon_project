from django.shortcuts import render

from apps.quiz.models import QuizPick4
from apps.articles.models import Article


# Create your views here.
def quiz_detail(request, pk):
    article = Article.objects.get(pk=pk)
    quiz = QuizPick4.objects.get(pk=pk)

    context = {"article": article, "quiz": quiz}

    return render(request, "quiz_detail.html", context)
