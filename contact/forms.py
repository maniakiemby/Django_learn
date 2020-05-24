from django import forms

from .models import Contact


class ContactModelForm(forms.ModelForm):
    class Meta:
        model  = Contact
        fields = [
            'title',
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower()  == 'abc':
            raise forms.ValidationError("This is not a validation title")
        return title