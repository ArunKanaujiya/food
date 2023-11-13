from WebApp.models import Company
from django import forms
class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=[
            'Company_Name',
            'Company_logo',
            'Company_city',
        ]

