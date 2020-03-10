from rest_framework import serializers
from .models import Professor

class ModuleSerializer(serializer.ModelSerializer):
    class Meta:
        model = Module
        fields = ("name","code")

# class ProfessorSerializer(serializer.ModelSerializer):
#     class Meta:
#         model = Professor
#         fields
