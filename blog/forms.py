from django import forms
from django.forms import modelformset_factory
from .models import Blog, Content


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog

        fields = ("title",)

        widgets = {"title": forms.TextInput(attrs={"placeholder": "A beautiful blog!"})}


ContentFormSet = modelformset_factory(
    Content,
    fields=("text",),
    extra=2,
    widgets={"text": forms.TextInput(attrs={"placeholder": "New content goes here"})},
)
