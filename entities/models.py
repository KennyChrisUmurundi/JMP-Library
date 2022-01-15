from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from library.models import Ebook, Library
from django.contrib.postgres.fields import JSONField


class bought_items(models.Model):

    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    item_file = models.FileField()
    date = models.DateTimeField(default=timezone.now)
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class paypal_data(models.Model):
    data = JSONField()
