from django.urls import path
from questions.views import IndexView


urlpatterns = [
    path("", IndexView, name="questions"),
]