from rest_framework import routers, serializers, viewsets

from Profile.models import ProfileModel
from Profile.models import CiudadModel
from Profile.models import GeneroModel
from Profile.models import OcupacionModel
from Profile.models import EstadoModel
from Profile.models import EstadoCivilModel

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CiudadModel
        fields = ('__all__')

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroModel
        fields = ('__all__')

class OcupacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcupacionModel
        fields = ('__all__')

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoModel
        fields = ('__all__')        

class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivilModel
        fields = ('__all__') 

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')

      