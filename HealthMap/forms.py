from django import forms

class LookupForm(forms.Form):
    autocomplete                   = forms.CharField()

