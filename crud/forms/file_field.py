from django import forms
from ..models.file_field import File


class File_forms(forms.ModelForm):
    names = [
        ("USA", "United states"),
        ("CA", "Canada"),
        ("FR", "France"),
    ]
    name = forms.ChoiceField(choices=names)

    file = forms.FileField(required=False)

    class Meta:
        model = File
        fields = [
            "name",
            "file",
        ]
        widgets = {"name": forms.Select(attrs={"class": "hover:bg-green-500"})}
