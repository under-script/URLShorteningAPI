from rest_framework import serializers

from api.models import Shorten


class ShortenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shorten
        fields = '__all__'
        read_only_fields = ['id', 'short_url']
