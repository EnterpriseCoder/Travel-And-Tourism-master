"""myfirstpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.PackageListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.PackageDetailView.as_view(),name='detail'),
    path('xx/', views.index, name='index'),
    #url(r'^create/$',views.UserCreateView.as_view(),name='create'),
    #path('',views.IndexView.as_view(),name='home'),
    path('myapp/',include('myapp.urls',namespace='myapp')),
    url(r'^users/$',views.users,name='users'),
    path('auto/',views.IView.as_view(),name='auto'),
    path('hakkımızda/', views.index2, name='index2'),
    path('hikayemiz/', views.index12, name='index12'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
