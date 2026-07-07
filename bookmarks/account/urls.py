from django.urls import include,path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
#     # Previous custom login URL (commented out)
#     # path('login/', views.user_login, name='login'),
#      # Built-in Django login / logout class-based views
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     # Change password URLs
#     path('password-change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
#     path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
#      # reset password urls
#     path('password-reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
#     path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
#     path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
#     path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
#     # Dashboard home view
#     path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
 ]
