from questions.models import Answer
from django import forms
from questions.models import Question

class AnswerForm(forms.Form):
    answers = forms.ModelChoiceField(queryset=None, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        if 'question_id' in kwargs and kwargs['question_id'] is not None:
            question_id = kwargs.pop('question_id')
            super().__init__(*args, **kwargs)
            queryset = Question.objects.get(pk=question_id).answer_set.all()
            self.fields['answers'].queryset = queryset