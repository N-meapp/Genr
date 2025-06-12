from django import forms
from .models import *

class JobApplicationForm(forms.ModelForm):
    job_position = forms.ModelChoiceField(
        queryset=Career.objects.all(),
        empty_label="Select Job Position",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'phone_number', 'job_position', 'cv']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'cv': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


