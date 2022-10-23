from rest_framework import serializers,generics
from .models import Paper

class PaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paper
        fields = "__all__"



