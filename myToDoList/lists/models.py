from django.db import models

class ToDo(models.Model):
    title = models.TextField(default='')
    completed = models.BooleanField(default = False)
    priority = models.PositiveIntegerField(default = 1)
    due = models.DateField(null = True, default = None)

    def __str__(self):
        return self.title
