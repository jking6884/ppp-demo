from django.db import models
from core.models import (
    User,
    Company
)


class Loan(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    user = models.ForeignKey(User, related_name='loan_user', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='loan_company', on_delete=models.CASCADE)
    loan_num = models.IntegerField()
    funding_date = models.DateField()
    loan_amount = models.DecimalField(max_digits=19, decimal_places=2)


class Document(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    loan = models.ForeignKey(Loan, related_name='documents', on_delete=models.CASCADE)
    external_id = models.CharField(max_length=255, null=True, blank=True)
