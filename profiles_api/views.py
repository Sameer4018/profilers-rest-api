from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (GET, POST, PATCH, PUT, DELETE)',
        'Is similar to a traditional Django View',
        'Gives you most control over application logic',
        'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello World!', 'an_apiview':an_apiview})
