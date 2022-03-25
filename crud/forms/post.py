from django import forms
from ..models import Post
from datetime import date

# class PostForm(forms.ModelForm):
#     post_date = forms.DateTimeField(input_formats=['%Y-%m-%d'], initial=date.today,
#     )
#     title = forms.CharField(max_length=20, required=True)
#     body = forms.CharField(
#         widget=forms.Textarea,
#         required=True,
#     )

#     class Meta:
#         model = Post
#         fields = [
#             "post_date"
#             "title",
#             "body",
#         ]
