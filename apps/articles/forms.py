from django import forms
from django.forms.widgets import TextInput

from apps.articles.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "color": TextInput(attrs={"type": "color"}),
        }
