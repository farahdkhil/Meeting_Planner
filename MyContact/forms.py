from django import forms

class ContactForm2(forms.Form):
    firstname = forms.CharField(max_length=10)
    lastname = forms.CharField(max_length=10)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
