from django.shortcuts import render
from .models import Poll, Question

def IndexView(request):
    polls = Poll.objects.all()
    context = {"polls": polls}
    return render(request, "questions/index.html", context)

def PollView(request, pk):
    poll = Poll.objects.get(pk=pk)
    first_question = poll.question_set.get()
    context = {
        "poll": poll,
        "first_question": first_question,
        "questions_num": poll.question_set.all().count(),
    }
    return render(request, "questions/poll.html", context)

def QuestionView(request, pk):
    question = Question.objects.get(pk=pk)
    answers = question.answer_set.all()
    context = {
        "question": question,
        "answers": answers,
    }
    return render(request, "questions/question.html", context)
