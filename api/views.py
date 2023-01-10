from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from .models import Candidate, AdverseEmail, CourtSearchReport
from .serializers import CandidateModelSerializer, AdverseEmailModelSerializer, CourtSearchReportModelSerializer


class CandidatesListView(ListAPIView):
    queryset = Candidate.objects.all().order_by('id')
    serializer_class = CandidateModelSerializer


class ChargesListView(ListAPIView):
    queryset = CourtSearchReport.objects.all().order_by('id')
    serializer_class = CourtSearchReportModelSerializer


class AdverseActionEmailView(APIView):
    """
    This endpoint is used to send the email.
    """

    def post(self, request, format=None):
        charges = request.data.get('charges', [])
        candidate_id = request.data.get('candidate_id', None)

        # Fetch the candidate instance
        candidate_instance = Candidate.objects.filter(id=candidate_id).last()
        if not candidate_instance:
            raise APIException("Candidate record was not found.")

        if not len(charges):
            raise APIException("Atleast one charge should selected.")

        # Json body for charges
        json_charges = {
            "charges": charges
        }

        email_body = f"Dear {candidate_instance.first_name} {candidate_instance.last_name},\nYou recently authorized checkr-bpo (“the company”) to obtain consumer reports and/or invistigate consumer reportsabout you from a consumer reporting agency. The Company is considering taking action in whole or in past on information in such report(s) including the following specific items identified in the report prepared by Checkr, Inc."
        for charge in charges:
            email_body += f"\n-{charge}"
        email_body += f"\n\nIf you wish to dispute the accuracy of the information in the report directly with the consumer reporting agency(i.e., the source of the informationcontained in the report), you should contact the agency identifield above directly.\n\nSincerely, Checkr-bpo"

        # Persist record
        record = AdverseEmail(
            candidate=candidate_instance,
            recepient_email=candidate_instance.email_id,
            content=email_body,
            charges=charges
        )
        record.save()

        serializer = AdverseEmailModelSerializer(record)

        return Response(serializer.data)
