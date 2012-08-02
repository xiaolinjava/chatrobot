from django import forms
from jjechat.books.models import Publisher

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
    