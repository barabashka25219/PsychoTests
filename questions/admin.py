from django.contrib import admin
from .models import Question

class AdminQuestion(admin.ModelAdmin):
    fieldsets = [
        ("Question description", {"fields": ["header", "text"]}),
    ]

admin.site.register(Question, AdminQuestion)