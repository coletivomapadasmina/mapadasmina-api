from candidates.models import Candidate
from candidates.serializers import CandidateSerializer
from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from candidates.models import Candidate, Party, GenderIdentity
from candidates.serializers import CandidateSerializer, PartySerializer, GenderIdentitySerializer


class CandidateList(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class GenderIdentityViewSet(viewsets.ModelViewSet):
    queryset = GenderIdentity.objects.all()
    serializer_class = GenderIdentitySerializer
