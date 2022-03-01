from django.shortcuts import render
from api_app.models import Phonelist, BuyPlatforms
from api_app.serializers import PhonelistSerializer, BuyPlatformsSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class PhonelistView(APIView):

    def get(self, request):
        Phonelist = Phonelist.objects.all()
        serializer = PhonelistSerializer(Phonelist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PhonelistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

class PhonelistDetailView(APIView):
    
    def get(self, request, pk):
        Phonelist = Phonelist.objects.get(pk=pk)
        serializer = PhonelistSerializer(Phonelist)
        return Response(serializer.data)

    def put(self, request, pk):
        Phonelist = Phonelist.objects.get(pk=pk)
        serializer = PhonelistSerializer(Phonelist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        Phonelist = Phonelist.objects.get(pk=pk)
        Phonelist.delete()

class PhonelistView(APIView):

    def get(self, request):
        Phonelist = Phonelist.objects.all()
        serializer = PhonelistSerializer(Phonelist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PhonelistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

class PhonelistDetailView(APIView):
    
    def get(self, request, pk):
        Phonelist = Phonelist.objects.get(pk=pk)
        serializer = PhonelistSerializer(Phonelist)
        return Response(serializer.data)

    def put(self, request, pk):
        Phonelist = Phonelist.objects.get(pk=pk)
        serializer = PhonelistSerializer(Phonelist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        Phonelist = Phonelist.objects.get(pk=pk)
        Phonelist.delete()