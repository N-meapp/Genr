from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import os
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

def validate_strict_email(value):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, value):
        raise ValidationError("Enter a valid email address like your@email.com.")

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



class ContactFormData(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'required': True,
            'pattern': '[A-Za-z ]+',
            'title': 'Name should only contain letters and spaces',
            'placeholder': 'Your Name'
        })
    )
    email = forms.EmailField(
        validators=[validate_strict_email],
        widget=forms.EmailInput(attrs={
            'required': True,
            'placeholder': 'your@email.com'
        })
    )
    mobile = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'required': True,
            'pattern': '[0-9]{10}',
            'title': 'Enter a 10-digit mobile number',
            'placeholder': '10-digit mobile number'
        })
    )
    enquiry = forms.ChoiceField(
        choices=[
            ('Power And Energy', 'Power And Energy'),
            ('Automation', 'Automation'),
            ('Cold Storage', 'Cold Storage'),
            ('Genr Smart', 'Genr Smart'),
            ('Genr Careers', 'Genr Careers'),
        ],
        widget=forms.Select(attrs={
            'required': True
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'required': True,
            'pattern': '^[A-Za-z0-9 \n\r]+$',  # Allow letters, numbers, and spaces ONLY
            'title': 'Message should only contain letters, numbers, and spaces',
            'placeholder': 'Your message',
            'rows': 1
        
        })
    )





class Request_Service(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'required': True,
            'placeholder': 'Enter Your Name',
            'class': 'form-control'
        })
    )

    email = forms.EmailField(
        validators=[validate_strict_email],
        widget=forms.EmailInput(attrs={
            'required': True,
            'placeholder': 'your@email.com'
        })
    )

    phone_number = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'required': True,
            'placeholder': '10-digit mobile number',
            'class': 'form-control'
        })
    )

    services = forms.ChoiceField(
        choices=[
            ('Product/Service Quality', 'Product/Service Quality'),
            ('Billing & Payments', 'Billing & Payments'),
            ('Damaged/Defective Product', 'Damaged/Defective Product'),
            ('Genr Smart', 'Genr Smart'),
            ('Others (Specify)', 'Others'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    special_note = forms.CharField(
        widget=forms.Textarea(attrs={
            'required': True,
            'placeholder': 'Your message',
            'class': 'form-control',
            'rows': 1
        })
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match(r'^[A-Za-z ]+$', name):
            raise forms.ValidationError("Name can only contain letters and spaces.")
        return name

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if not re.match(r'^\d{10}$', phone):
            raise forms.ValidationError("Enter a valid 10-digit mobile number.")
        return phone

    def clean_special_note(self):
        note = self.cleaned_data['special_note']
        if not re.match(r'^[A-Za-z0-9 \n\r]+$', note):
            raise forms.ValidationError("Special note can only contain letters and numbers (no special characters).")
        return note



def validate_strict_email(value):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, value):
        raise ValidationError("Enter a valid email address like your@email.com.")
    


def validate_pdf_file(file):
    # File size check (500KB = 512000 bytes)
    if file.size > 512000:
        raise ValidationError("File size must be under 500KB")

    # File extension check (optional but recommended)
    ext = os.path.splitext(file.name)[1].lower()
    if ext != '.pdf':
        raise ValidationError("Only PDF files are allowed")



class CareerForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z ]+$',
                message='Name should only contain letters and spaces.'
            )

        ],
        widget=forms.TextInput(attrs={
            'required': True,
            'pattern': '[A-Za-z ]+',
            'placeholder': 'Your Name'
        })
    )

    email = forms.EmailField(
        validators=[validate_strict_email],
        widget=forms.EmailInput(attrs={
            'required': True,
            'placeholder': 'your@email.com'
        })
    )

    mobile = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Enter a valid 10-digit mobile number.'
            )
        ],
        widget=forms.TextInput(attrs={
            'required': True,
            'placeholder': '10-digit mobile number'
        })
    )

    job_position = forms.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 \n\r]+$',
                message='Job position should only contain letters, numbers, and spaces.'
            )
        ],
        widget=forms.TextInput(attrs={
            'required': True,
            'title': 'Only letters, numbers, and spaces allowed',
            'pattern': '^[A-Za-z0-9 \n\r]+$',
            'placeholder': 'Job Position'
        })
    )

    resume = forms.FileField(
        required=True,
        validators=[validate_pdf_file],
        widget=forms.ClearableFileInput(attrs={
            'accept': 'application/pdf',
            'required': True
        })
    )


class ReviewForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=50,
        validators=[
            RegexValidator(r'^[A-Za-z ]+$', 'Name should only contain letters and spaces.')
        ],
        widget=forms.TextInput(attrs={
            'required': True,
            'pattern': '[A-Za-z ]+',
            'placeholder': 'Your Name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'required': True,
            'placeholder': 'your@email.com'
        })
    )

    work = forms.CharField(
        required=False,
        max_length=100,
        validators=[
            RegexValidator(r'^[A-Za-z0-9 ]+$', 'Only letters, numbers, and spaces allowed.')
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Your Position'})
    )

    company_name = forms.CharField(
        required=False,
        max_length=100,
        validators=[
            RegexValidator(r'^[A-Za-z ]+$', 'Only letters and spaces allowed.')
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Your Company'})
    )

    customer_id = forms.CharField(
        required=False,
        max_length=15,
        validators=[
            RegexValidator(r'^[A-Za-z0-9]+$', 'Only letters and numbers allowed.')
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Customer ID'})
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'required': True,
            'placeholder': 'Your review...',
            'rows': 3
        }),
        validators=[
            RegexValidator(r'^[A-Za-z0-9 .,!?@#&()\'"\-\n\r]+$', 'Invalid characters in message.')
        ]
    )

    rating = forms.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        widget=forms.NumberInput(attrs={
            'required': True,
            'min': '0',
            'max': '5',
            'step': '0.5',
            'placeholder': 'e.g. 4.5'
        })
    )

    class Meta:
        model = CustomerReview
        fields = ['full_name', 'email', 'customer_id', 'work', 'company_name', 'message', 'rating']