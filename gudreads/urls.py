from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(
        template_name='gudreads/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/gudreads'), name='logout'),
    path('create_account/', views.create_account, name='create_account'),
    path('change_password/', auth_views.PasswordChangeView.as_view(
        template_name='gudreads/registration/change_password.html', success_url='done/'), name='change_password'),
    path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='gudreads/registration/change_password_done.html'),
         name='change_password_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='gudreads/registration/password_reset.html', html_email_template_name='gudreads/registration/password_reset_email.html', success_url='done/', subject_template_name='gudreads/registration/password_reset_email_subject.html'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='gudreads/registration/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='gudreads/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/confirm_done/', auth_views.PasswordResetCompleteView.as_view(template_name='gudreads/registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('user_books/', views.user_book_list_page, name='user_book_list_page'),
    path('user_books/update/<int:id>', views.update_book, name='update_book'),
    path('user_books/delete/<int:id>', views.delete_book, name='delete_book'),
    path('user_books/edit/<int:id>', views.edit_book, name='edit_book'),
    path('browse_books', views.browse_books, name='browse_books'),
    path('user_books/ajax/autocomplete',
         views.get_goodreads_results, name='ajax_autocomplete')
]
