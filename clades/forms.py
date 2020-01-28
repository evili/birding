from django import forms

class CladesSearchForm(forms.Form):
    search = forms.CharField(label='Search')


