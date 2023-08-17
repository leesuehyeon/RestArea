"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

#이미지 업로드
from django.conf.urls.static import static
from django.conf import settings
from info import views

from django.urls import re_path as url
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', include('info.urls')),
    path('review/', include('review.urls')),
    path('common/', include('common.urls')),
    path('map/', include('map.urls')),
    path('check/',include('check.urls')),
    path('', include('main.urls')),
    path('', views.index, name='index'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

#오류 발생 시 호출
# handler400 = 'common.views.error400'
# handler403 = 'common.views.error403'
# handler404 = 'common.views.error404'
# handler500 = 'common.views.error500'