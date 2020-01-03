from django.urls import path
from . import views

urlpatterns = [
    path("", views.total_book),
    path("oreilly-books/", views.oreilly_books),
    path("book/", views.BookAPIView.as_view()),
    path("classic/", views.BookAPIViewClassic.as_view()),
]

