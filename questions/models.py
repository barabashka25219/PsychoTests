from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

def image_path(instance, filename):
        """ 
        Get file path for 'upload_to' argument
        """
        print('#########################')
        print(dir(instance))
        print('save to' + f' {instance.__class__.__name__}/{instance.id}/${filename}')
        return f'{instance.__class__.__name__}/{instance.id}/{filename}'

class Poll(models.Model):
    header = models.CharField(max_length=80)
    description_text = models.TextField(max_length=1000)
    passed_poll_num = models.IntegerField()
    image_poll = models.FileField(blank=True, null=True, upload_to=image_path)

    @admin.display(description='Questions')
    def get_questions_number(self):
        return len(self.question_set.all())
    
    @admin.display(description='Completed by users')
    def get_passed_poll_num(self):
        return self.passed_poll_num

    def __str__(self):
        return self.header

class Question(models.Model):
    header = models.CharField(max_length=80)
    question_text = models.TextField(max_length=200)
    poll = models.ManyToManyField(Poll)
    number_in_poll = models.PositiveIntegerField()

    @admin.display(description='Poll')
    def get_poll(self):
        return self.poll.get()

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

    @admin.display(description='Poll')
    def get_poll(self):
        return self.question.poll.get()
    
    @admin.display(description='Question')
    def get_question_header(self):
        return self.question.header

    def __str__(self):
        return f'{self.question.header}: {self.answer.answer_text}'