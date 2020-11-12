from django.db import models


class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    email = models.EmailField('Email', help_text="User email", unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    address_one = models.CharField(max_length=255, blank=True, null=True)
    address_two = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=64, blank=True, null=True)


class Company(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    address_one = models.CharField(max_length=255, blank=True, null=True)
    address_two = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=64, blank=True, null=True)

    phone = models.CharField(max_length=30, blank=True, null=True)

    num_of_employees = models.IntegerField()

    primary_contact = models.ForeignKey(User, related_name='primary_contact', on_delete=models.CASCADE)

    payroll_costs = models.DecimalField(max_digits=19, decimal_places=2)
    business_mortgage_interest_payments = models.DecimalField(max_digits=19, decimal_places=2)
    business_rent_or_lease_payments = models.DecimalField(max_digits=19, decimal_places=2)
    business_utility_payments = models.DecimalField(max_digits=19, decimal_places=2)

    wage_reductions_amount = models.IntegerField(default=0)

    reference_period = models.DateField()
    num_of_employees_at_reference = models.IntegerField()

    sba_number = models.IntegerField(unique=True)
    ein = models.IntegerField(unique=True)
    dba = models.CharField(max_length=255)
    entity_name = models.CharField(max_length=255)

    @property
    def total_costs(self):
        return self.payroll_costs + \
            self.business_mortgage_interest_payments + \
            self.business_rent_or_lease_payments + \
            self.business_utility_payments

    @property
    def fte_reduction_quotient(self):
        return self.num_of_employees / self.num_of_employees_at_reference

    @property
    def payroll_cost_60_percent_requirement(self):
        return self.payroll_costs / .60
