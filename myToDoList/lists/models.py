from django.db import models

class ToDo(models.Model):
    text = models.TextField(default='')

    def __str__(self):
        return self.text
