"""
All the forms are here
"""

from django import forms
from .models import Vision

class VisionForm(forms.ModelForm):
    """A dummy docstring."""
    class Meta:
        """A dummy docstring."""
        model = Vision
        fields = ['vision_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vision_name'].label = ''