from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^create$', UserCreate.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', UserUpdate.as_view(), name='update'),
    url(r'^detail/(?P<pk>\d+)/$', UserDetail.as_view(), name='detail'),
    url(r'^delete/(?P<pk>\d+)/$', UserDelete.as_view(), name='delete'),
    url(r'^list$', UserList.as_view(), name='list'),
    # access action
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LoginView.as_view(), name='logout'),
    url(r'^$', private, name='index'),
]
