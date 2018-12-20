from django import forms
from .models import Project
from froala_editor.widgets import FroalaEditor

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'content']
        widgets = {
            'content': FroalaEditor(),
            'title': forms.TextInput(
                attrs={
                    'style': 'height: 30px; margin-bottom:15px; width:300px;',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            )
        }