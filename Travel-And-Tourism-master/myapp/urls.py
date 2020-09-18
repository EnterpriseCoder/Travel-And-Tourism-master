from django.urls import path
from django.conf.urls import url
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('',views.PackageListView.as_view(),name='list_app'),
    url(r'^(?P<pk>\d+)/$',views.PackageDetailView.as_view(),name='detail'),
    
]
