from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    header = models.CharField(max_length=80)
    description_text = models.TextField(max_length=1000)
    passed_poll_num = models.IntegerField()

    def __str__(self):
        return self.header

class Question(models.Model):
    header = models.CharField(max_length=80)
    question_text = models.TextField(max_length=200)
    poll = models.ManyToManyField(Poll)
    number_in_poll = models.PositiveIntegerField()

    def __str__(self):
        if len(self.header) > 50:
            return self.header[:50]
        return self.header
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=50)

    def __str__(self):
        return self.answer_text
    
class QuestionResult(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.question.header}: {self.answer.answer_text}'