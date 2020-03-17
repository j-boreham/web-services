from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, Http404
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_200_OK
from .models import Module, Professor, Rating, ModuleInstance
from .serializers import ModuleSerializer, UserSerializer, ModuleInstanceSerializer
from decimal import Decimal, ROUND_HALF_UP
import json




class register(APIView):
    '''Handling the registration of a new user and adding
        to the User table'''
    @csrf_exempt
    def post(self,request,format=None):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.create_user(username,email,password)
        return Response(status=status.HTTP_201_CREATED)


class loginUser(APIView):
    '''Class containing method to handle login'''
    @csrf_exempt
    def post(self,request,format =None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request,user)
            token, _ = Token.objects.get_or_create(user = user)
            return Response({'token': token.key})
        else:
            return Response({'token':'User does not exist, please register'},status=HTTP_404_NOT_FOUND)


class listModules(APIView):
    '''Class for returning the list of all modules at the uni'''
    def get(self,request,format=None):

        output_list = []
        modules = ModuleInstance.objects.all()
        for module in modules:
            #Get professors into a list for creating the Dict
            profList=[]
            profs = module.professors.all()
            for prof in profs:
                profList.append(prof.uid + ", "+ prof.first_name + " " + prof.last_name)

            #Create the instance for adding to the list of all modules.
            instanceDict = {"code":module.code.code, 'name': module.code.name, 'year' : str(module.year), 'semester' : str(module.semester), 'professors': profList}

            output_list.append(instanceDict)

        output_dict = {'module_list':output_list}

        return Response(output_dict)

    #Post requests not accepted for this format.
    def post(self,request,format = None):
        return Response(request.data, status = status.HTTP_400_BAD_REQUEST)



class viewProfessors(APIView):
    '''Get the average rating of all professors'''
    def get(self,request,format = None):
        output_list =[]
        # For each professor, get their ratings and take an avaerage of all of them. adding their info to a list
        professors = Professor.objects.all()
        for prof in professors:
            total_score = 0
            number_of_ratings = 0

            ratings = prof.rating_set.all()
            for r in ratings:
                total_score += r.rating
                number_of_ratings +=1

            average_score = Decimal(total_score/number_of_ratings).quantize(Decimal('1.'),rounding = ROUND_HALF_UP)
            instanceDict = {'professor_first':prof.first_name, 'professor_last': prof.last_name, 'professor_id':prof.uid, 'avg_score': int(average_score) }
            output_list.append(instanceDict)

        output_dict = {'professor_ratings':output_list}

        return Response(output_dict)

    #Post requests not accepted for this format.
    def post(self,request,format = None):
        return Response(request.data, status = status.HTTP_400_BAD_REQUEST)



class professorModuleScore(APIView):
    ''' Return the average score of a professor in a given module'''
    def get(self,request,format = None):

        #Get all the ratings of the professor then filter down
        prof_id = request.query_params['professor_uid']
        module_code = request.query_params['module_code']
        prof =  Professor.objects.get(uid = prof_id)
        module_ratings = prof.rating_set.filter(module_instance__code__code = module_code )

        if len(module_ratings)==0:
            return Response("No data for that Module with that Professor")

        total_score = 0
        number_of_ratings = 0
        for v in module_ratings:
            total_score += v.rating
            number_of_ratings += 1

        module_score = Decimal(total_score/number_of_ratings).quantize(Decimal('1.'),rounding = ROUND_HALF_UP)
        output_dict = {'professor_first':prof.first_name, 'professor_last': prof.last_name, 'professor_id':prof.uid, 'avg_score': str(module_score)}
        return Response(output_dict)

    #Post requests not accepted for this format.
    def post(self,request,format = None):
        return Response(request.data, status = status.HTTP_400_BAD_REQUEST)



class rateProfessor(APIView):
    '''Rating a professor for a particular module instance they have taught'''

    #Check the client has sent a token for authentication with the request, deny access if not.
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
        #Get data fields
        module_code = request.data.get("module_code")
        prof_id = request.data.get("professor_uid")
        year = request.data.get("year")
        semester = request.data.get("semester")
        rating = request.data.get("rating")

        #Check if the user has selected a valid module that has been taught by the professor
        checked_module = get_object_or_404(Module, code = module_code)
        checked_professor = get_object_or_404(Professor, uid = prof_id)
        module_instance = get_object_or_404(ModuleInstance, code = checked_module,
                                            year = year, semester = semester,
                                            professors = checked_professor)

        #Create the rating instance
        Rating.objects.create(rating = rating, professor_uid = checked_professor,
                            module_instance = module_instance)

        return Response("Rating Successfully submitted")
