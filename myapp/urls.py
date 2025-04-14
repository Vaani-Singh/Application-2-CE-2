from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),             # Home page
    path('login/', views.login_view, name='login'),         # Login page
    path('signup/', views.signup_view, name='signup'),      # Signup page
    path('report/', views.report_view, name='report'),      # Report page
    path('settings/', views.settings_view, name='settings') # Settings page
]
