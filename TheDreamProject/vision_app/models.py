from django.db import models

# Create your models here.
class Vision(models.Model):
    vision_name = models.CharField(max_length=255)

class Goal(models.Model):
    goal_name = models.CharField(max_length=255)
    vision = models.ForeignKey(Vision, on_delete=models.CASCADE)
    # vision_id = vision
    # Query for a Specfic Vision
    # Match the Foreignkey to the Vision 
    # Add the goal_name to the goal table
    # Add the Foreign Key to the Goal Table


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    goals = models.ManyToManyField(Goal)
