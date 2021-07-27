from django.db import models
from django.utils import timezone


class bought_items(models.Model):
	item = models.CharField(max_length=200)
	item_file = models.FileField()
	date = models.DateTimeField(default=timezone.now)

