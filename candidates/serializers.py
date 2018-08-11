from rest_framework import serializers
from candidates.models import Candidate, Party, Role, Picture

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('name', 'slug','number', 'bio','instagram','latitude', 'longitude','facebookURL',
        'campaignUrl','supportUrl','age','electedBefore','role','party','picture')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('role_id', 'name')

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('picture_id', 'url')    
    
class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('party_id', 'name', 'number')