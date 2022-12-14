"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
'''
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
'''
from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url
from . import views,search

app_name = 'comment'
 
urlpatterns = [
    url(r'^$',views.login),
    url(r'^fanc/$', views.fanc),
    url(r'^get-text/$', views.get_text),
    url(r'^search-post/$', search.search_post),
    #url(r'^get-video/$', views.show_video),
    #url(r'admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('captcha/', include('captcha.urls')),

]

