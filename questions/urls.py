from django.urls import path
from questions.views import IndexView

app_name = "questions"

urlpatterns = [
    path("", IndexView, name="questions"),
]