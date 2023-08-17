from django.urls import path

from . import views

app_name="check"

urlpatterns = [
    path('create/',views.create,name='create'),
    path('index/',views.index,name='index'),
]