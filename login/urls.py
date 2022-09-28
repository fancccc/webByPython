from django.urls import path
from . import views
#from django.conf.urls import url

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('show_video/',views.show_video, name='show_video'),
    path('to_picture/',views.to_picture, name='to_picture'),
    path('to_pubg/',views.to_pubg, name='to_pubg'),
    path('query_pubg/',views.query_pubg, name='query_pubg'),
    path('to_video/',views.to_video, name='to_video'),
    path('to_BallPool/',views.to_BallPool, name='to_BallPool'),
    path('to_dnf/',views.to_dnf, name='to_dnf'),
    path('submit1/',views.submit1, name='submit1'),
    path('translate/',views.translate, name='translate'),
    path('to_translate/',views.to_translate, name='to_translate'),
    path('to_draw/',views.to_draw, name='to_draw'),
    path('draw/',views.draw, name='draw'),
    path('poetry/',views.poetry, name='poetry'),
    #url(r'^get-video/$', views.show_video)
]
