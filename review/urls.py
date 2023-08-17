from django.urls import path

from . import views

app_name = "review"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('modify/<int:review_id>/', views.modify, name='modify'),
    path('delete/<int:review_id>/', views.delete, name='delete'),
]