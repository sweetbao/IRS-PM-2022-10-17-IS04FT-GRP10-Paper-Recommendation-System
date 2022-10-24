from rest_framework import serializers,generics
from .models import UserPrefer,UserViewRecord

class PreferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserPrefer
        fields = "__all__"



class ViewRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserViewRecord
        fields = "__all__"
