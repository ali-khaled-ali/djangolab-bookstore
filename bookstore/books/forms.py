from django import forms
from .models import Book, Isbn


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ["isbn",]