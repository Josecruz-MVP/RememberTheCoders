"""
All the forms are here
"""

from django import forms
from .models import Vision, Goal, Task

class VisionForm(forms.ModelForm):
    """A dummy docstring."""
    class Meta:
        """A dummy docstring."""
        model = Vision
        fields = ['vision_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vision_name'].label = ''

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['goal_name, vision_id '].label = ''

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['task_name'].label = ''