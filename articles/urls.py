from django.urls import re_path
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    re_path(r'^$', views.article_list, name='list'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
    path('category/<category>/', views.CatListView.as_view(), name="category"),
]
