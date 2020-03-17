
from django.urls import path
from . import views

urlpatterns = [

    path('listModules/', views.listModules.as_view(), name='modules'),
    path('login/', views.oginUser.as_view(), name='login'),
    path('register/',views.register.as_view(), name='register'),
    path('view/',views.viewProfessors.as_view(), name='professors'),
    path('specific-module-average/', views.professorModuleScore.as_view() ,name=' professor_module_score'),
    path('rate/', views.rateProfessor.as_view(), name = 'module_instance_score'),

]
