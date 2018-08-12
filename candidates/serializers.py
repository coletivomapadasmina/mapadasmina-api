from rest_framework import serializers

from candidates.models import Candidate, Party, Role, Picture, Cause, Ethnicity, GenderIdentity

class CauseSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Cause
        fields = ('id', 'title', 'description')

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

class GenderIdentitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GenderIdentity
        fields = ('id', 'name')

class EthnicitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ethnicity
        fields = ('id', 'name')


class CandidateSerializer(serializers.ModelSerializer):
    causes = CauseSerializer(many=True)
    previousRole = RoleSerializer()
    role = RoleSerializer()
    genderIdentity = GenderIdentitySerializer()
    picture = PictureSerializer()
    party = PartySerializer()
    ethnicity = EthnicitySerializer()

    class Meta:
        model = Candidate
        fields = ('id', 'name', 'electionName', 'slug', 'number', 'bio',
        'instagram', 'latitude', 'longitude', 'facebookUrl', 'campaignUrl',
        'supportUrl', 'age', 'electedBefore', 'previousRole', 'role',
        'ethnicity', 'genderIdentity', 'causes', 'party', 'picture')
