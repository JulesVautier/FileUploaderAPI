from django.db import models

class File(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    storage_name = models.CharField(max_length=200, blank=True, default='')
    storage_location = models.CharField(max_length=1000, blank=True, default='')

    class Meta:
        ordering = ('created',)