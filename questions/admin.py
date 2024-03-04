from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.StackedInline):
    model = Answer

class AdminQuestion(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["header", "question_text"]}),
    ]

    inlines = [AnswerInline,]

admin.site.register(Question, AdminQuestion)