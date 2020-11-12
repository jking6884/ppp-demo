from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .serializers import (
    ForgivenessRequestSerializer,
    CreateForgivenessRequestSerializer,
    UploadForgivenessRequestLoanDocumentsSerializer
)
from .models import (
    ForgivenessRequest
)
from .exceptions.exceptions import (
    ForgivenessSdkBadRequest
)
from .services.loan_forgiveness_service import (
    LoanForgivenessService
)


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.all()


class ForgivenessRequestViewSet(BaseViewSet):
    serializer_class = ForgivenessRequestSerializer
    model = ForgivenessRequest

    @action(detail=False, methods=['POST'], name='Create Forgiveness Request For Loan')
    def create_request(self, request, *args, **kwargs):
        serializer = CreateForgivenessRequestSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ForgivenessSdkBadRequest as ex:
            return Response(ex.args[0].get("detail"), status=ex.args[0].get("status_code"))

    @action(detail=False, methods=['POST'], name='Upload Documents For Loan')
    def upload_loan_document(self, request, *args, **kwargs):
        serializer = UploadForgivenessRequestLoanDocumentsSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ForgivenessSdkBadRequest as ex:
            return Response(ex.args[0].get("detail"), status=ex.args[0].get("status_code"))

    @action(detail=False, methods=['GET'], name='Lookup and Validate Forgiveness Request')
    def lookup_and_validate_forgiveness_request(self, request, *args, **kwargs):
        if not self.request.query_params.get('sba_number'):
            return Response("SBA Number is required", status=status.HTTP_400_BAD_REQUEST)

        result = LoanForgivenessService.lookup_and_validate_forgiveness_request(self.request.query_params.get('sba_number'))
        return Response(result)
