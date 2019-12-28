from django.urls import path
from . import views

urlpatterns = [
    path("", views.total_book),
    path("book/", views.BookAPIView.as_view()),
    path("classic/", views.BookAPIViewClassic.as_view()),
]

