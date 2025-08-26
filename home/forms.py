from django import forms

Class ContactForms(forms.Form):
    name = forms.CharField(max_length = 50)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget = forms.TextArea)

class ContactFormsOne(form.Form):
    email = forms.EmailField()
    message = forms.CharField(widget = forms.TextArea)