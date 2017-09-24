from django import forms
from .models import UserInfo, DesignerIdea


class DesignerIdeaForm(forms.ModelForm):
    class Meta:
        model = DesignerIdea
        fields = ['title', 'description']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['weekday_daytime', 'weekday_night', 'weekends_daytime', 'weekends_night', 'user_type']
