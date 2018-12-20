from django.db import models
from froala_editor.fields import FroalaField

class Project(models.Model):
    title = models.CharField(max_length=100)
    content = FroalaField(theme='dark')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

