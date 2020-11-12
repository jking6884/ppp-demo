from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    UserSerializer,
    CompanySerializer,
)
from .models import (
    User,
    Company,
)


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.all()


class UserViewSet(BaseViewSet):
    serializer_class = UserSerializer
    model = User


class CompanyViewSet(BaseViewSet):
    serializer_class = CompanySerializer
    model = Company
