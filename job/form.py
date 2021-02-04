from django.db import models
from django import forms
from .models import Apply


class Applyform(forms.ModelForm):
    class Meta:
        model=Apply
        exclude=['job','create_at']