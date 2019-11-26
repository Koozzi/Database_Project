from django import forms
from .models import *

class reviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields =('review_text',)

