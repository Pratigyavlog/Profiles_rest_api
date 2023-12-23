from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response

class HelloApiView(APIView):
  def get(self,request,format=None):
    an_apiview=[
      'Uses HTTP method function as GET, POST, DELETE, PUT ',
      'It mapped manually to the URLS',
      'It is similar to a traditional HTTP Request'
    ]

    return Response({'message':'Hello', 'an_apiview':an_apiview})
