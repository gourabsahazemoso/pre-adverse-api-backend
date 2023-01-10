from rest_framework import serializers
from .models import Candidate, AdverseEmail, CourtSearchReport


class CandidateModelSerializer(serializers.ModelSerializer):
    adverse_state = serializers.SerializerMethodField('get_adverse_state')

    class Meta:
        model = Candidate
        fields = '__all__'

    def get_adverse_state(self, data):
        return AdverseEmail.objects.filter(candidate__id=data.id).count() > 0


class AdverseEmailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdverseEmail
        fields = '__all__'


class CourtSearchReportModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtSearchReport
        fields = '__all__'
