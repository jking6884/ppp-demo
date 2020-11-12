from django.db import models

from loan.models import (
    Loan
)


class ForgivenessRequest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    loan = models.ForeignKey(Loan, related_name='forgiveness_request', on_delete=models.CASCADE, unique=True)
    external_id = models.CharField(max_length=255)
