from rest_framework import serializers
from .models import Share
class shareSerializer(serializers.ModelSerializer):
    class Meta:
        model=Share
        fields='__all__'
        depth=1