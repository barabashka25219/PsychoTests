from django.shortcuts import render, redirect
from django.http import Http404
from .models import Poll, Question, QuestionResult, Answer
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
    
    try:
        first_question = poll.question_set.all().order_by('number_in_poll')[0:1].get()
    except Question.DoesNotExist:
        raise Http404

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
            answer_id = request.POST['answers']
            answer = Answer.objects.get(pk=answer_id)
            
            # Find exist result if user has completed the poll earlier
            try:
                question_result = QuestionResult.objects.filter(user=request.user).get(question=question)
                question_result.answer = answer
            except QuestionResult.DoesNotExist:
                question_result = QuestionResult(question=question, answer=answer, user=request.user)
            
            question_result.save()
            
            # If it's last question then render end template
            if question.number_in_poll == len(Question.objects.all()) - 1:
                return render(request, 'questions/poll_end.html', context={'poll': question.poll.get()})
            
            next_question = Question.objects.get(number_in_poll=question.number_in_poll+1)
            
            return redirect("polls:question", pk=next_question.pk)

    context = {
            "question": question,
            "answer_form": answer_form,
        }   
    return render(request, "questions/question.html", context=context)