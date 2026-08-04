from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:

        model = Book

        fields = [
            "title",
            "author",
            "isbn",
            "category",
            "publisher",
            "publish_date",
            "quantity",
            "available_quantity",
            "cover",
            "description",
            "language",
            "pages",
        ]

        widgets = {

            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "author": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "isbn": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "category": forms.Select(attrs={
                "class": "form-select"
            }),

            "publisher": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "publish_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "quantity": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "available_quantity": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "cover": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4
            }),

            "language": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "pages": forms.NumberInput(attrs={
                "class": "form-control"
            }),

        }