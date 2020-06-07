from django import forms
from admin_dashboard.models import Book

class BookUploadForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_title','book_description','book_image','book_rates','book_commit_id','book_publish']
