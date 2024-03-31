from django.db import models
from django.contrib.auth.models import User
from questions.models import image_path
from PsychoTestProject import settings
import shutil
import os.path
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(
        choices = (
            ('M', 'Male'),
            ('F', 'Female'),
        ),
        max_length=1,
        blank=True,
        help_text='Пол'
    )
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=800, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to=image_path)

    # IT'S NOT WORKING, this method is not used
    # by Django. Find out what removes entry from db
    # def delete(self, using=None, keep_parents=False):
    #     # media/Profile/user_id
    #     profile_folder = os.path.join(
    #         settings.MEDIA_ROOT,
    #         self.__class__.__name__,
    #         str(self.user_id)
    #     )

    #     print(f'Remove profile directory: {profile_folder}')

    #     try:
    #         shutil.rmtree(profile_folder)
    #     except FileNotFoundError:
    #         pass

    #     return super().delete(using=using, keep_parents=keep_parents)

# Remove folder by django signals
@receiver(pre_delete, sender=Profile)
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