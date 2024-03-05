from django.shortcuts import render
from .models import Poll

def IndexView(request):
    polls = Poll.objects.all()
    context = {"polls": polls}
    return render(request, "questions/index.html", context=context)