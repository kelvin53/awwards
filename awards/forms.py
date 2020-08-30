from .models import Project,Profile
from django import forms



#......

class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile']
class NewRateForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','title','image','description','link']
