from django import forms
from ..models import Post


class PostForm(forms.ModelForm):

    title = forms.CharField(max_length=20, required=True)
    author = forms.CharField(
        max_length=20,
        required=True,
    )
    body = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post
        fields = [
            "title",
            "author",
            "body",
        ]
