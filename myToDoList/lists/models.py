from django.db import models

class ToDo(models.Model):
    text = models.TextField(default='')
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.text
