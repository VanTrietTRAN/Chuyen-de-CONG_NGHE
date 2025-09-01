from django.urls import path
from . import views
from main.views import AboutView
from books.views import BookListView

urlpatterns = [
    path("", views.help_home, name="help_home"),

    path("about/", AboutView.as_view()),

    path("books/", BookListView.as_view()),


]


