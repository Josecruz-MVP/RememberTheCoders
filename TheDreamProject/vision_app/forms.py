from django import forms
from vision_app.models import Vision, Goal, Task

class VisionForm(forms.ModelForm):
    class Meta:
        model = Vision
        fields = ['vision_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['vision_name'].label = 'Add Vision'

