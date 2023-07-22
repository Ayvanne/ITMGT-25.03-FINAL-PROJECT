from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Incident(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=150)
    date_reported = models.DateTimeField(default=timezone.now)
    pictures = models.ImageField(upload_to='incident_pictures')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})