from django.urls import path, include
from questions.views import IndexView, PollView, QuestionView

app_name = "polls"

urlpatterns = [
    path("", IndexView, name="polls"),
    path("<int:pk>/", PollView, name="poll"),
    path("question/<int:pk>/", QuestionView, name="question"),
]