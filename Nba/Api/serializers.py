from django.db.models import fields
from rest_framework import serializers
from .models import *


class PlayerSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Player
        fields = '__all__'
    

