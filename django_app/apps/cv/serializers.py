from rest_framework import serializers
from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class SearchQuerySerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_null=True, allow_blank=True, default="")
