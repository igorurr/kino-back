"""KinoApi URL Configuration

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
from django.urls import include, path

from KinoApi.views import ( UserCountView, UserAuthView, UserRegistarationView, 
                            UserRestorePassView, UserMeView )

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/countusers', UserCountView.as_view(), name='countusers'),

    path('api/v1/user/auth',            UserAuthView.as_view(),             name='UserAuth'),
    path('api/v1/user/registration',    UserRegistarationView.as_view(),    name='UserRegistaration'),
    path('api/v1/user/restore_pass',    UserRestorePassView.as_view(),      name='UserRestorePass'),
    path('api/v1/user/me',              UserMeView.as_view(),               name='UserMe'),
]
