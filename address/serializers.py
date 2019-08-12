from rest_framework import serializers
from . import models


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = ('__all__')
        read_only_fields = ['id']


class CitySerializer(serializers.ModelSerializer):
    state = serializers.PrimaryKeyRelatedField(queryset=models.State.objects.all())

    class Meta:
        model = models.City
        fields = ('id', 'name', 'state')
        read_only_fields = ['id']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['state'] = StateSerializer(instance.state).data
        return response


class LocalitySerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(queryset=models.City.objects.all())

    class Meta:
        model = models.Locality
        fields = ('id', 'name', 'city')
        read_only_fields = ['id']
        validators = []

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['city'] = CitySerializer(instance.city).data
        return response


class AddressSerializer(serializers.ModelSerializer):
    locality = LocalitySerializer()

    class Meta:
        model = models.Address
        fields = ('company_name', 'building_number', 'postal_code', 'locality')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['locality'] = LocalitySerializer(instance.locality).data
        return response

    def create(self, validated_data):
        locality_data = validated_data.pop('locality')
        locality = models.Locality.objects.get_or_create(**locality_data)
        validated_data['locality'] = locality[0]
        instance = models.Address.objects.create(**validated_data)
        instance.save()
        return instance


class PostCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ('postal_code',)


class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ('company_name',)

