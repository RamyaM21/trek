from django.urls import path
from . import views
from .views import home_view  # ✅ Add this
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home_view, name='home'),   
   
  
    
    path('trek-type/<str:type>/', views.trek_type_view, name='trek_type'),


    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('district/<int:district_id>/', views.district_detail, name='district_detail'),
    path('trek/<int:trek_id>/', views.trek_detail, name='trek_detail'),

    # Password Reset Flow
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='core/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'), name='password_reset_complete'),
]
