from django.conf.urls import include, url

from rest_framework import routers

from .views import (
    UserViewSet,
    CompanyViewSet,
)

api_router = routers.SimpleRouter()
api_router.register(r'users', UserViewSet, basename='user')
api_router.register(r'companies', CompanyViewSet, basename='company')

urlpatterns = [
    url(r'', include(api_router.urls)),
]
