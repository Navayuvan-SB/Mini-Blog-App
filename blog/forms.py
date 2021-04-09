from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Blog, Content


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title']


class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['text']


AddBlogWithContentFormSet = inlineformset_factory(
    Blog, Content, form=ContentForm, extra=2)
