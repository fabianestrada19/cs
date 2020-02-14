from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Profile.models import ProfileModel
from Profile.serializer import ProfileSerializer

from Profile.models import CiudadModel
from Profile.serializer import CiudadSerializer

from Profile.models import GeneroModel
from Profile.serializer import GeneroSerializer

from Profile.models import OcupacionModel
from Profile.serializer import OcupacionSerializer

from Profile.models import EstadoModel
from Profile.serializer import EstadoSerializer

from Profile.models import EstadoCivilModel
from Profile.serializer import EstadoCivilSerializer

class CiudadList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = CiudadModel.objects.filter(delete = False)
        serializer = CiudadSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CiudadSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GeneroList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = GeneroModel.objects.filter(delete = False)
        serializer = GeneroSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneroSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
class OcupacionList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = OcupacionModel.objects.filter(delete = False)
        serializer = OcupacionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OcupacionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = EstadoModel.objects.filter(delete = False)
        serializer = EstadoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoCivilList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = EstadoCivilModel.objects.filter(delete = False)
        serializer = EstadoCivilSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoCivilSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
class ProfileList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ProfileModel.objects.filter(delete = False)
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        

# Create your views here.
