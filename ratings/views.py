from django.shortcuts import render
#from rest_framework import generics
#from .models import Professor,Module,Rating,User

from .models import Module, Professor, User, Rating


'''Returns the home page for RateMyProf '''

def home(request):
    return render(request, 'ratings/home.html',{})


#def login(request):


def listModules(request):
    modules = Module.objects.all()
    return render(request,'ratings/listModules.html',{'modules':modules})

'''Takes user post request of username, email, password passes them to the database to
to be stored'''
#@csrf_exempt
def handleRegisterRequest(request):
    return HttpResponse('Not here yet')




#def Login(request):


# class ListModules(generics.ListAPIView):
#     queryset = Module.objects.all()
#     serializer_class = ModuleSerializer
