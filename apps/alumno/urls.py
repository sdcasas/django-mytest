#!/usr/local/lib/python3.4
# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^create$', AlumnoCreate.as_view(), name='alumnoCreate'),
    url(r'^update/(?P<pk>\d+)/$', AlumnoUpdate.as_view(), name='alumnoUpdate'),
    url(r'^list$', AlumnoList.as_view(), name='alumnoList'),
    url(r'^detail/(?P<pk>\d+)/$', AlumnoDetail.as_view(), name='alumnoDetail'),
]
