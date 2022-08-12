from django.db import models

class Task(models.Model):
    name=models.CharField(max_length=30)
    task=models.CharField(max_length=30)
    def __str__(self):
        return self.name +' '+ self.task