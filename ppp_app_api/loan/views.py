from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    LoanSerializer
)
from .models import (
    Loan
)


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.all()


class LoanViewSet(BaseViewSet):
    serializer_class = LoanSerializer
    model = Loan
