
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [

    #path('',views.home, name = 'home'),
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('listModules/', views.listModules.as_view(), name='modules'),
    path('login/', views.loginUser.as_view(), name='login'),
    path('register/',views.register.as_view(), name='register'),
    path('view/',views.viewProfessors.as_view(), name='professors'),
    path('specific-module-average/', views.professorModuleScore.as_view() ,name=' professor_module_score'),
    path('rate/', views.rateProfessor.as_view(), name = 'module_instance_score'),

]
