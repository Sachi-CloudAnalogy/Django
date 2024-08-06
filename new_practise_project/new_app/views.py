from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from new_app import serializers

#Test API View
class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    #Returns a list of APIView features
    def get(self, request, format=None):
        an_apiview = ['uses HTTP methods as functions', 'is mapped manually to urls', 'get, post, patch, put, delete']

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    #Create a hello message with our name
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Handle updating an object
    def put(self, request, pk=None):
        return Response({'method': 'PUT'})
    
    #Handle a partial update of an object
    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})
    
    #Delete an object
    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})
    
    