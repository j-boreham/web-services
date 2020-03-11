from rest_framework import serializers
from .models import Professor, Module, ModuleInstance, Rating
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ("name","code")

class ModuleInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleInstance
        fields = ('code','year','semester','professors')



class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('uid')
