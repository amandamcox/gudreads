from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BookList


class CreateAccountForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50, required=True, help_text='Required')
    last_name = forms.CharField(
        max_length=50, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')


class AddBookToList(forms.ModelForm):
    book_name = forms.CharField(
        max_length=100, required=True, help_text='Enter a book title. Ex: Harry Potter and the Goblet of Fire')
    book_author = forms.CharField(
        max_length=100, required=False, widget=forms.HiddenInput())
    book_image = forms.URLField(
        max_length=300, required=False, widget=forms.HiddenInput())

    class Meta:
        model = BookList
        fields = ['book_name', 'book_author', 'book_image']


class EditBook(forms.ModelForm):
    book_name = forms.CharField(max_length=100, required=True,
                                help_text='Enter a book title. Ex: Harry Potter and the Goblet of Fire')
    book_description = forms.CharField(
        max_length=350, required=False, help_text='A brief description of the book. Max characters: 350')
    book_author = forms.CharField(
        max_length=100, required=False, help_text='Author\'s name of the entered book')
    book_image = forms.URLField(max_length=300, required=False,
                                help_text='Enter a URL for an image of the book cover')
    book_was_read = forms.BooleanField(
        required=False, label='Read this book?')

    class Meta:
        model = BookList
        fields = ['book_name', 'book_description',
                  'book_author', 'book_image', 'book_was_read']
