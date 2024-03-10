from django.shortcuts import render
from .models import Poll

def IndexView(request):
    polls = Poll.objects.all()
    context = {"polls": polls}
    return render(request, "questions/index.html", context)

def PollView(request, pk):
    poll = Poll.objects.get(pk=pk)
    context = {
        "poll": poll,
        "questions_num": poll.question_set.all().count(),
    }
    return render(request, "questions/poll.html", context)