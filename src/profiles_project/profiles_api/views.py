from . import models
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from rest_framework.authentication import TokenAuthentication
from . import permissions
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


class HelloApiView(APIView):
    
    serializer_class=serializers.HelloSerializer
    def get(self,request,format=None):
        an_apiview=[
                
                ]
        return Response({'message':'Hello','an_apiview':an_apiview})
                
    def post(self,request):
        serializer=serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
        return Response({'method':'put'})
    def patch(self,request,pk=None):
        return Response({'method':'patch'})
    def delete(request,pk=None):
        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """test api ViewSet."""
    def list(self,request):
        """return a hello message"""
        a_viewset=[
               "Monu Kumar",
                ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})

class UserProfileViewSet(viewsets.ModelViewSet):
    
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)
 
class LoginViewSet(viewsets.ViewSet):
    
    serializer_class=AuthTokenSerializer
    
    def create(self,request):
        return ObtainAuthToken().post(request)