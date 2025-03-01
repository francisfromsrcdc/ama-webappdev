from django import forms

class TextInputForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Your Text')