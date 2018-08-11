from rest_framework import serializers
from candidates.models import Candidate, Party, GenderIdentity

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('name', 'slug','number', 'bio','instagram','latitude', 'longitude','facebookURL',
        'campaignUrl','supportUrl','age','electedBefore')

""" class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'url')

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'name') """


class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'name', 'number')


class GenderIdentitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'name')

