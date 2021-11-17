from django.db import models
from dabase.models import UserProfile

class Task(models.Model):
    task_text = models.CharField(max_length=300)
    price = models.IntegerField()
    child = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='child_task')
    parent = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='parent_task')

    def __str__(self):
        return self.task_text
