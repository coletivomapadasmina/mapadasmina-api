from rest_framework import serializers
from candidates.models import Candidate, Party

class CandidateSerializer(serializers.Serializer):
    name=serializers.CharField()
    slug=serializers.CharField()
    party=serializers.CharField()
    number=serializers.CharField()
    latitude=serializers.CharField()
    longitude=serializers.CharField()

    def create(self,validated_data):
        """
        Creates and returns a new Candidate object
        """
        return Candidate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Candidate object, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.party = validated_data.get('party', instance.party)
        instance.number = validated_data.get('number', instance.number)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.save()
        return instance
    
    
class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'name', 'number')