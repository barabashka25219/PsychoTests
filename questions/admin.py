from django.contrib import admin
from .models import Question, Answer, Poll, QuestionResult

class AnswerInline(admin.StackedInline):
    model = Answer

class QuestionInline(admin.StackedInline):
    model = Question.poll.through

class AdminQuestion(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["header", "question_text", "poll"]}),
    ]

    list_display = ["number_in_poll", "header", "question_text"]
    inlines = [AnswerInline,]

class AdminPoll(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["header", "description_text", "passed_poll_num"]})
    ]

    list_display = ["pk", "header", "description_text"]
    inlines = [QuestionInline]

class AdminQuestionResult(admin.ModelAdmin):
    list_display = ['pk', '__str__', 'user']

admin.site.register(Question, AdminQuestion)
admin.site.register(Poll, AdminPoll)
admin.site.register(QuestionResult, AdminQuestionResult)