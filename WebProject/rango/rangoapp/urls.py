from django.conf.urls import url
from rangoapp import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.page, name='page'),
    re_path(
        r'^category/(?P<category_name_url>\w+)/$',
        views.category,
        name='category'),
]