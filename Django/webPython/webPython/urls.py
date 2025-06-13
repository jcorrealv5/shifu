"""
URL configuration for webPython project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path , include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('appDemo01/', include('appDemo01.urls')),
    path('appDemo02/', include('appDemo02.urls')),
    path('appDemo03/', include('appDemo03.urls')),
    path('appDemo04/', include('appDemo04.urls')),
    path('appDemo05/', include('appDemo05.urls')),
    path('appDemo06/', include('appDemo06.urls')),
    path('appDemo07/', include('appDemo07.urls')),
    path('appDemo08/', include('appDemo08.urls')),
    path('appDemo09/', include('appDemo09.urls')),
    path('appDemo10/', include('appDemo10.urls')),
    path('appDemo11/', include('appDemo11.urls')),
    path('appDemo12/', include('appDemo12.urls')),
    path('appDemo13/', include('appDemo13.urls')),
    path('appDemo14/', include('appDemo14.urls')),
    path('appDemo15/', include('appDemo15.urls')),
    path('appDemo16/', include('appDemo16.urls')),
    path('appDemo17/', include('appDemo17.urls')),
    path('appDemo18/', include('appDemo18.urls')),
    path('appDemo19/', include('appDemo19.urls')),
    path('appDemo20/', include('appDemo20.urls')),
    path('appDemo21/', include('appDemo21.urls')),
    path('appDemo22/', include('appDemo22.urls')),
    path('appDemo23/', include('appDemo23.urls')),
    path('appDemo24/', include('appDemo24.urls')),
    path('appDemo28/', include('appDemo28.urls')),
    path('servicio01/', include('servicio01.urls')),
    path('appDemo29/', include('appDemo29.urls')),
    path('servicio02/', include('servicio02.urls')),
    path('appDemo30/', include('appDemo30.urls')),
    path('servicio03/', include('servicio03.urls')),
    path('appDemo31/', include('appDemo31.urls')),
    path('servicio04/', include('servicio04.urls')),
    path('appDemo32/', include('appDemo32.urls')),
    path('wsDemo02/', include('wsDemo02.urls')),
    path('wsDemo03/', include('wsDemo03.urls')),
]
