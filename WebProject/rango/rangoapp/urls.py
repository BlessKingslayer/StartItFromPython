from django.conf.urls import url
from rangoapp import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.page, name='page'),
]