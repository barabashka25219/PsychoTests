from django.shortcuts import render, redirect
from .models import Poll, Question
from .forms import AnswerForm
from django.views.decorators.http import require_http_methods, require_GET

def LOG_DEBUG(func, message):
    print(f'[DEBUG] {func.__name__}: {message}')

@require_GET
def IndexView(request):
    polls = Poll.objects.all()
    context = {"polls": polls}
    return render(request, "questions/index.html", context)

@require_GET
def PollView(request, pk):
    poll = Poll.objects.get(pk=pk)
    first_question = poll.question_set.all()[0]
    print(first_question)
    context = {
        "poll": poll,
        "first_question": first_question,
        "questions_num": poll.question_set.all().count(),
    }
    return render(request, "questions/poll.html", context)

@require_http_methods(['GET', 'POST'])
def QuestionView(request, pk):
    question = Question.objects.get(pk=pk)

    if request.method == 'GET':
        answer_form = AnswerForm(question_id=pk)
        
    else:
        answer_form = AnswerForm(request.POST, question_id=pk)
        if answer_form.is_valid():
            LOG_DEBUG(QuestionView, "Form is valid")
            return redirect("polls:question", pk=pk+1)

    context = {
            "question": question,
            "answer_form": answer_form,
        }   
    return render(request, "questions/question.html", context=context)