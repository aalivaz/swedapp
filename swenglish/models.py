from django.db import models
from django.utils import timezone

# Create your models here.

class Wordlist(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    swe_word = models.CharField(max_length=200)
    singular_swe = models.CharField(max_length=200)
    sing_definitive_swe = models.CharField(max_length=200)
    plural_swe = models.CharField(max_length=200)
    plural_definitive_swe = models.CharField(max_length=200)
    definition = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

