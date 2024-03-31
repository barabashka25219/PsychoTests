from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from PsychoTestProject import settings
import shutil
import os.path

def image_path(instance, filename):
        """ 
        Get file path for 'upload_to' argument
        """
        return f'{instance.__class__.__name__}/{instance.user_id}/{filename}'

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
    

# Remove folder by django signals
@receiver(pre_delete, sender=Poll)
def profile_folder_delete(sender, instance, **kwargs):
    instance.avatar.delete(save=False)

    # media/Profile/user_id
    profile_folder = os.path.join(
        settings.MEDIA_ROOT,
        instance.__class__.__name__,
        str(instance.user_id)
    )

    print(f'Remove profile directory: {profile_folder}')

    try:
        shutil.rmtree(profile_folder)
    except FileNotFoundError:
        pass


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