"""misitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# Aqui empieza
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
#from perfiles import views

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/',include('jet.dashboard.urls', 'jet-dashboard')),

#    url(r'^accounts/', include('registration.backends.default.urls')),
#    url(r'^admin/', include('admin.site.urls')),

#     url(r'^welcome/$', views.welcome),
#     url(r'^register/$', views.register),
#     url(r'^login/$', views.login),
#     url(r'^logout/$', views.logout),


    url(r'^admin/', admin.site.urls),
    url(r'', include('polls.urls')),



]


admin.site.site_title = "Administracion"
admin.site.site_header = "Administracion de Encuestas"
