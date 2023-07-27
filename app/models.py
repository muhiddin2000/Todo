from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.TextField()
    start = models.DateTimeField()
    finish = models.DateTimeField()
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title