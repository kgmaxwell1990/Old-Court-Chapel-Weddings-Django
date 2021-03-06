"""old_court_chapel_weddings URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from home.views import get_index, get_gallery, get_vendors, get_info, contact

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name="index"),
    url(r'^gallery/', get_gallery, name="gallery"),
    url(r'^vendors/', get_vendors, name="vendors"),
    url(r'^info/', get_info, name="info"),
    url(r'^contact/', contact, name="contact"),
]
