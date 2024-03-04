from django.db import models

class Question(models.Model):
    header = models.CharField(max_length=80)
    text = models.TextField(max_length=200)

    def __str__(self):
        if len(self.header) > 50:
            return self.header[:50]
        return self.header

