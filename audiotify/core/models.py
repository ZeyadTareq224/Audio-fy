from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Audible(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.CharField(max_length=4)
    book = models.FileField()
    is_converted = models.BooleanField(default=False)

    def __str__(self):
        return f"USER: {self.author} book: {self.book} page: {self.page}"

    def get_audio_name(self):
        return f"{self.book}_page{self.page}"
