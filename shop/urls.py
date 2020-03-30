from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'shop'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.product_list, name='product_list'),
    # change password urls
    path('password_change/',
         auth_views.PasswordChangeView.as_view(
            template_name='shop/password_change_form.html',
            success_url="/password_change/done/",
         ), name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
            template_name='shop/password_change_done.html'
         ), name='password_change_done'),
    # reset password urls
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name="shop/password_reset_form.html",
             email_template_name="shop/password_reset_email.html",
             subject_template_name="shop/password_reset_subject.txt",
             success_url="/password-reset-done/",
         ),
         name='password_reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="shop/password_reset_done.html"
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="shop/password_reset_confirm.html",
             success_url="/password-reset-complete/",
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="shop/password_reset_complete.html"
         ),
         name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
