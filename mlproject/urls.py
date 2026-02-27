from django.contrib import admin
from django.urls import path, include
from predictor.views import signup

from django.contrib.auth import views as auth_views
from predictor import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/', signup, name='signup'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Password Reset
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),

    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset_done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    path('', include('predictor.urls')),
    path('profile/', views.profile_view, name='profile'),

]