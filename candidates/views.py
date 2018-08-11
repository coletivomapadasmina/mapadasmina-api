from candidates.models import Candidate
from candidates.serializers import CandidateSerializer
from rest_framework import generics


class CandidateList(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer