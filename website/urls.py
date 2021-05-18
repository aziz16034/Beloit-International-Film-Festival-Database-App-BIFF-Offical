"""mysitebiff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('home/', views.home, name='home'),
    path('', auth_views.LoginView.as_view(template_name='Log-In.html'), name='login'),
    # path('', views.login, name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('login/', auth_views.LoginView.as_view(template_name='Login-In.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('home/about/', views.about, name='about'),
    path('home/contact/', views.contact, name='contact'),
    path('database/',views.database,name='database'),
    path('', include("django.contrib.auth.urls")),
    path('database2/', views.database2, name='database2'),
    path('<int:id>', views.detail, name='detail'),
    path('dashboard/', views.dashboard, name='dashboard'),




]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)