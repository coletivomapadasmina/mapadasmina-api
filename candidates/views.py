from rest_framework import viewsets
from candidates.models import Candidate, Party, GenderIdentity, Role, Picture, Cause
from candidates.serializers import CandidateSerializer, PartySerializer, RoleSerializer, PictureSerializer, CauseSerializer, GenderIdentitySerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class CauseViewSet(viewsets.ModelViewSet):
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer


class GenderIdentityViewSet(viewsets.ModelViewSet):
    queryset = GenderIdentity.objects.all()
    serializer_class = GenderIdentitySerializer
