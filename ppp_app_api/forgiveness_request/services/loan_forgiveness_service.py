from django.conf import settings

from forgiveness_request.PPPForgivenessSDK.client import Client
from forgiveness_request.exceptions.exceptions import (
    ForgivenessSdkBadRequest,
)
from forgiveness_request.models import (
    ForgivenessRequest
)
from loan.models import (
    Document
)

class LoanForgivenessService:
    @staticmethod
    def create_forgiveness_request_for_loan(loan):
        payload = LoanForgivenessService.build_forgiveness_request_payload(loan)
        return LoanForgivenessService.perform_create_request(loan, payload)

    @staticmethod
    def upload_loan_documents(loan,
                              document_type,
                              name,
                              document):
        client = LoanForgivenessService.get_client()

        document = LoanForgivenessService.convert_document(document)

        loan_documents_api = client.loan_documents

        result = loan_documents_api.create(name, document_type, loan.forgiveness_request.get().external_id, document)

        if result['status'] == 201:
            document = Document(
                loan=loan,
                external_id=result['data']['etran_loan']['slug'],
            )
            return document.save()
        else:
            raise ForgivenessSdkBadRequest(result['data'])

    @staticmethod
    def lookup_and_validate_forgiveness_request(sba_number):
        client = LoanForgivenessService.get_client()

        lookup_api = client.validations

        result = lookup_api.list(sba_number=sba_number)

        if result['status'] == 200:
            return result['data']

    @staticmethod
    def build_forgiveness_request_payload(loan):
        return {
            'bank_notional_amount': float(loan.loan_amount),
            'sba_number': loan.company.sba_number,
            'loan_number': loan.loan_num,
            'entity_name': loan.company.entity_name,
            'ein': loan.company.ein,
            'funding_date': str(loan.funding_date),
            'address1': loan.company.address_one,
            'address2': loan.company.address_two if loan.company.address_two else '-',
            'dba_name': loan.company.dba,
            'phone_number': loan.company.phone,
            'forgive_fte_at_loan_application': loan.company.num_of_employees,
            'forgive_amount': float(LoanForgivenessService.calculate_forgive_amount(loan)),
            'forgive_fte_at_forgiveness_application': loan.company.num_of_employees,
            'primary_email': loan.company.primary_contact.email,
            'primary_name': "{} {}".format(loan.company.primary_contact.first_name, loan.company.primary_contact.last_name),
            'ez_form': False,
            'forgive_lender_confirmation': True,
            'forgive_lender_decision': 1,
            's_form': True
        }

    @staticmethod
    def perform_create_request(loan, payload):
        client = LoanForgivenessService.get_client()

        forgiveness_api = client.forgiveness_requests

        result = forgiveness_api.create(**payload)

        if result['status'] == 201:
            forgiveness_request = ForgivenessRequest(
                external_id=result['data']['etran_loan']['slug'],
                loan=loan
            )
            return forgiveness_request.save()
        else:
            if 'etran_loan' in result.get('data').keys():
                raise ForgivenessSdkBadRequest({
                    'status_code': result['data']['status_code'],
                    'detail': result['data']['etran_loan']
                })
            else:
                raise ForgivenessSdkBadRequest(result['data'])

    @staticmethod
    def calculate_forgive_amount(loan):
        total_payroll = loan.company.payroll_costs
        total_expenses = loan.company.total_costs
        reduction_quotient = loan.company.fte_reduction_quotient
        modified_total = float(total_expenses) / reduction_quotient
        return min(total_payroll, modified_total, loan.loan_amount)

    @staticmethod
    def get_client():
        return Client(
            access_token=settings.SBA_FORGIVENESS_CONFIG.get('access_token'),
            vendor_key=settings.SBA_FORGIVENESS_CONFIG.get('vendor_key'),
            environment=settings.SBA_FORGIVENESS_CONFIG.get('environment'),
        )

    @staticmethod
    def convert_document(document):
        return document.file.read()
