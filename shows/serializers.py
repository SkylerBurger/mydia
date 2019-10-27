from rest_framework import serializers

from .models import Show, ShowCopy


class ShowCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowCopy
        fields = ['platform', 'form']


class ShowSerializer(serializers.ModelSerializer):
    copies = ShowCopySerializer(many=True, read_only=True)

    class Meta:
        model = Show
        fields = ['title', 'season', 'release_year', 'copies']