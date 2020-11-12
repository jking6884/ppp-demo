from rest_framework import serializers

from .models import (
    ForgivenessRequest,
)
from loan.models import (
    Loan
)
from .services.loan_forgiveness_service import LoanForgivenessService


class ForgivenessRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForgivenessRequest
        fields = '__all__'


class CreateForgivenessRequestSerializer(serializers.Serializer):
    loan = serializers.PrimaryKeyRelatedField(queryset=Loan.objects.all())

    def create(self, validated_data):
        LoanForgivenessService.create_forgiveness_request_for_loan(validated_data.get('loan'))


class UploadForgivenessRequestLoanDocumentsSerializer(serializers.Serializer):
    loan = serializers.PrimaryKeyRelatedField(queryset=Loan.objects.all())
    document_type = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    document = serializers.FileField()

    def create(self, validated_data):
        LoanForgivenessService.upload_loan_documents(**validated_data)


class LookupAndValidateForgivenessRequestSerializer(serializers.Serializer):
    sba_number = serializers.IntegerField()
