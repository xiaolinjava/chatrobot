from django import forms
from jjechat.qAnda.models import QAndA

class QAndA(forms.ModelForm):
    class Meta:
        model = QAndA
    