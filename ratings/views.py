from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, Http404
from django.views.decorators.http import require_http_methods
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import authentication, permissions, status
from rest_framework.permissions import  IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Module, Professor, Rating, ModuleInstance
from .serializers import ModuleSerializer, UserSerializer, ModuleInstanceSerializer

'''Returns the home page for RateMyProf '''

def home(request):
    return render(request, 'ratings/home.html',{})


class register(APIView):
    '''Handling the registration of a new user and adding
        to the User table'''
    @csrf_exempt
    def post(self,request,format=None):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

class login(APIView):
    '''Allows a registered user to login and leave ratings'''
    #print (user_for_token)value
    def post(self,request):

        serializer = UserSerializer(data=request.data)
        user_for_token = User.objects.get(username = request.data.get('username'))
        token = Token.objects.create(user = user_for_token)
        print(token.key)
        pass


class listModules(APIView):
    '''Class for returning the list of all modules at the uni'''
    def get(self,request,format=None):
        modules = ModuleInstance.objects.all()
        serializer_class = ModuleInstanceSerializer(modules,many = True)
        return Response(serializer_class.data)



class view(APIView):

    '''Get the average rating of all professors'''
    def get(self,request,format = None):
        professors = Professor.objects.all()

        for prof in professors:
            ratings = Rating.objects.filter(professor_uid = prof.get(uid))
            print(ratings)
        pass

class average(APIView):
    def get(self,request,format = None):
        return Response(status.HTTP_400_BAD_REQUEST)



class rate(APIView):
    '''Rating a professor for a particular module instance they have taught)'''
    authentication_classes = [TokenAuthentication]
    permissions = [IsAuthenticated]
    def post(self,request,format=None):
        return Response(status.HTTP_400_BAD_REQUEST)
