from django.conf.urls import url, include

from .views import (create,
					detail,
					listall)

urlpatterns = [
	url(r'^create/', create),
	url(r'^detail', detail),
	url(r'^listall', listall),
]