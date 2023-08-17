from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:info_id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]