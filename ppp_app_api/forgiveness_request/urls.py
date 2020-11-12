from django.conf.urls import include, url

from rest_framework import routers

from .views import (
    ForgivenessRequestViewSet
)

api_router = routers.SimpleRouter()
api_router.register(r'forgiveness-requests', ForgivenessRequestViewSet, basename='forgiveness-request')

urlpatterns = [
    url(r'', include(api_router.urls)),
]
