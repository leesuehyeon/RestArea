from django.urls import path

from . import views

app_name = "info"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:info_id>/', views.detail, name='detail'),
    path('vote/<int:info_id>/', views.vote, name='vote'),
]