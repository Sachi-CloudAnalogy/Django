from rest_framework.views import APIView
from rest_framework.response import Response

#Test API View
class HelloApiView(APIView):

    #Returns a list of APIView features
    def get(self, request, format=None):
        an_apiview = ['uses HTTP methods as functions', 'is mapped manually to urls', 'get, post, patch, put, delete']

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    

