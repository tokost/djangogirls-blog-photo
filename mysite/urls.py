"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings        # pridane kvoli kombinacii blogov a foto
from django.conf.urls.static import static  # pridane kvoli kombinacii blogov a foto

# from django.contrib.auth import views     zmenene na toto
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    re_path(r'^admin/', admin.site.urls),   # treba dat prec include a zatvorky
#    path('admin/', admin.site.urls),
    re_path(r'^accounts/login/$', LoginView.as_view(), name='login'),   # pouzit LoginView.as_view()
    re_path(r'^accounts/logout/$', LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    path('', include('blog.urls')),     # kvoli fotografiam
]

# pridane kvoli kombinacii blogov a foto
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)