from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count
from .models import BookList
from .forms import CreateAccountForm, AddBookToList, EditBook


def index(request):
    return render(request, 'gudreads/index.html')


def create_account(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                raise forms.ValidationError()
    else:
        form = CreateAccountForm()
    return render(request, 'gudreads/registration/create_account.html', {'form': form})


def user_book_list_page(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:

        if request.method == 'POST':
            form = AddBookToList(request.POST)
            if form.is_valid():
                new_book_save = form.save(commit=False)
                new_book_save.user = request.user
                new_book_save.save()
            return redirect('user_book_list_page')
        else:
            form = AddBookToList()
            books_by_user = BookList.objects.filter(user=request.user)
            return render(request, 'gudreads/user_book_list.html', {'form': form, 'books_by_user': books_by_user})


def update_book(request, id):
    book = BookList.objects.get(id=id)
    if request.GET['rating']:
        rating = request.GET['rating']
        book.book_rating = rating
        book.save()
        return redirect('user_book_list_page')


def delete_book(request, id):
    book = BookList.objects.get(id=id)
    book.delete()
    return redirect('user_book_list_page')


def edit_book(request, id):
    book = BookList.objects.get(id=id)
    if request.method == 'GET':
        form = EditBook()
        form.fields['book_name'].initial = book.book_name
        form.fields['book_description'].initial = book.book_description
        form.fields['book_author'].initial = book.book_author
        form.fields['book_image'].initial = book.book_image
        form.fields['book_was_read'].initial = book.book_was_read
        return render(request, 'gudreads/edit_book.html', {'form': form, 'book': book})
    else:
        form = EditBook(request.POST)
        if form.is_valid():
            book.book_name = form.cleaned_data.get('book_name')
            book.book_description = form.cleaned_data.get('book_description')
            book.book_author = form.cleaned_data.get('book_author')
            book.book_image = form.cleaned_data.get('book_image')
            book.book_was_read = form.cleaned_data.get('book_was_read')
            book.save()
        return redirect('user_book_list_page')


def browse_books(request):
    top_rated_books = BookList.objects.filter(
        book_rating__isnull=False).order_by('-book_rating')[:5]
    recently_added_books = BookList.objects.order_by('-created_at')[:5]
    most_read_books = BookList.objects.filter(book_was_read=True).values(
        'book_name').annotate(Count('pk')).order_by('-pk__count')[:5]
    return render(request, 'gudreads/browse_books.html', {'top_rated_books': top_rated_books, 'recently_added_books': recently_added_books, 'most_read_books': most_read_books})
