from django.core.serializers import serialize
from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import generics
from django.views import View
from django.db.models import Count

from books.models import Book
from .serializers import BookSerializer


def total_book(request):
    count = Book.objects.aggregate(number_of_books=Count("title"))
    return JsonResponse(count, safe=False)


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookAPIViewClassic(View):
    def get(self, request):
        books = list(Book.objects.all().values())
        return JsonResponse(books, safe=False)

    def post(self, request):
        b = Book(**request.data)
        b.save()
        return JsonResponse(model_to_dict(b), safe=False)
