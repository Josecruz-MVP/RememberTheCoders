from django.db import models

# Create your models here.
class Vision(models.Model):
    vision_name = models.CharField(max_length=255)

class Goal(models.Model):
    goal_name = models.CharField(max_length=255)
    vision = models.ForeignKey(Vision, on_delete=models.CASCADE)

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    goals = models.ManyToManyField(Goal)
