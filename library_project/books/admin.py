from django.contrib import admin
from .models import Book


class BookAdminModel(admin.ModelAdmin):
    list_display = ("title", "author", "isbn", "subtitle")


admin.site.register(Book, BookAdminModel)
