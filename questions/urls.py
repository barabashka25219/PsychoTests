from django.urls import path
from questions.views import IndexView, PollView

app_name = "polls"

urlpatterns = [
    path("", IndexView, name="polls"),
    path("<int:pk>/", PollView, name="poll"),

]