from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for example
from app_example.serializers import ExampleSerializer
# Example model
from app_example.models import Example


# Create your views here.
class example(APIView):
    @csrf_exempt
    def get(self, request):
        return Response({'result': 'Example'}, status=200)
    
class login(APIView):
    @csrf_exempt
    def post(self, request):
        return Response({'result': request.data}, status=200)