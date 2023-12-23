from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .import serializers
class HelloApiView(APIView):
  
  serializer_class=serializers.HelloSerializer
  def get(self,request,format=None):
    an_apiview=[
      'Uses HTTP method function as GET, POST, DELETE, PUT ',
      'It mapped manually to the URLS',
      'It is similar to a traditional HTTP Request'
    ]
    return Response({'message':'Hello', 'an_apiview':an_apiview})

  def post(self, request):
    serializer = serializers.HelloSerializer(data=request.data)

    if serializer.is_valid():
        name = serializer.data.get('name')
        message = 'Hello {0}'.format(name)
        return Response({'message': message})
    else:
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self,request,pk=None):
    return Response({'message':'put'})

  def patch(self, request, pk=None):
    return Response({'message':'Patch'})  

  def delete(self, request,pk=None):
    return Response({'method':'Delete'})  





  
