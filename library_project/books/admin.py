from django.contrib import admin
from .models import Book, Publisher


class BookAdminModel(admin.ModelAdmin):
    list_display = ("title", "isbn")


class PublisherAdminModel(admin.ModelAdmin):
    list_display = ("name", "website")


admin.site.register(Book, BookAdminModel)
admin.site.register(Publisher, PublisherAdminModel)
