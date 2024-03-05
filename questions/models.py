from django.db import models

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

    def __str__(self):
        if len(self.header) > 50:
            return self.header[:50]
        return self.header
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=50)

    def __str__(self):
        return self.answer_text