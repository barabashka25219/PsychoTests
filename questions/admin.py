from django.contrib import admin
from .models import Question, Answer, Poll, QuestionResult

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

    fieldsets = [
        (
            "Answer",
            {
                "fields": ["answer_text",],
            }
        )
    ]

class QuestionInline(admin.TabularInline):
    model = Question.poll.through

    related_name = "question"
    
    fieldsets = [
        (
            None,
            {
                "fields": ["question",]
            }
        )
    ]

    verbose_name_plural = "Questions"
    verbose_name = "Question"
    extra = 0

class AdminQuestion(admin.ModelAdmin):
    fieldsets = [
        (
            "Question", 
            {
                "fields": ["number_in_poll", "header", "question_text", "poll"]
            }
        ),
    ]

    list_display = [
        "get_poll", 
        "get_number", 
        "get_header", 
        "get_question_text"
    ]

    def get_number(self, obj):
        return obj.number_in_poll
    
    def get_header(self, obj):
        return obj.header
    
    def get_question_text(self, obj):
        return obj.question_text
    
    get_header.short_description = 'Question'
    get_number.short_description = 'Number'
    get_question_text.short_description = 'Content'

    inlines = [AnswerInline,]

class AdminPoll(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["header", "description_text", "passed_poll_num"]})
    ]

    list_display = [
        "header", 
        "get_passed_poll_num", 
        'get_questions_number',
    ]

    inlines = [QuestionInline]

class AdminQuestionResult(admin.ModelAdmin):
    list_display = [
        'get_poll',
        'get_question_header',
        'answer',
        'user',
    ]

admin.site.register(Question, AdminQuestion)
admin.site.register(Poll, AdminPoll)
admin.site.register(QuestionResult, AdminQuestionResult)