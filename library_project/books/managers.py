from django.db import models


class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class OreillyBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(publisher__name="Oreilly")
