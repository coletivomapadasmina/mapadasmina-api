from rest_framework import serializers

from candidates.models import Candidate, Party, Role, Picture, Cause

from candidates.models import Candidate, Party, GenderIdentity

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('name', 'slug','number', 'bio','instagram','latitude', 'longitude','facebookUrl',
        'campaignUrl','supportUrl','age','electedBefore','role','party','picture')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'url')


class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'name', 'number')


class CauseSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Cause
        fields = ('id', 'title', 'description')


class GenderIdentitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GenderIdentity
        fields = ('id', 'name')
