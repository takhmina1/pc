"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .yasg import urlpatterns as yasg_urls
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user.urls')),
    path('api/', include('balance.urls')),
    path('news/', include('news.urls')),
    path('fag/', include('fag.urls')),
    path('applications/', include('applications.urls')),
    path('contact/', include('contact.urls')),
    path('skitka/', include('skitka.urls')),
    path('inves/', include('inves.urls')),
    path('partner/', include('partner.urls')),
    path('exchange/', include('exchange.urls')),
    path('trading/', include('trading.urls')),
    path('reviews/', include('reviews.urls')),
    path('kycam/', include('kycaml.urls')),
]
urlpatterns += yasg_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)