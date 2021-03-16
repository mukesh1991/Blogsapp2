from django import forms

class EmailsendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(widget=forms.Textarea)

from .models import Comments
class commentform(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["name","email",'body']