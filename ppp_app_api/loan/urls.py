from django.conf.urls import include, url

from rest_framework import routers

from .views import (
    LoanViewSet
)

api_router = routers.SimpleRouter()
api_router.register(r'loans', LoanViewSet, basename='loan')

urlpatterns = [
    url(r'', include(api_router.urls)),
]
