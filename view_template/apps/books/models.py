from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateTimeField()

    class Meta:
        ordering = ["-publication_date"]
        get_latest_by = "publication_date"

    def __str__(self) -> str:
        return self.title


