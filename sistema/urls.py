from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

ws = [
    url(r'^usr/', include('apps.users.restfull.urls')),
    url(r'^alu/', include('apps.alumno.restfull.urls')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls,),
    url(r'^alumno/', include('apps.alumno.urls', namespace='alumno')),
    url(r'^users/', include('apps.users.urls', namespace='users')),
    url(r'^ws/', include(ws, namespace='ws')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
