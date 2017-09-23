from django import forms
from .models import UserInfo, DesignerIdea


class DesignerIdeaForm(forms.ModelForm):
    class Meta:
        model = DesignerIdea
        fields = ['title', 'description']
