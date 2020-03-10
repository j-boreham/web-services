
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name = 'home'),
    path('listModules/', views.listModules, name='modules'),
    path('login/',views.login, name = 'login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.handleRegisterRequest, name='register'),
    path('viewProfs/',views.viewProfessors, name='professors'),
    path('profModule/', views.professorModuleScore,name=' professor_module_score'),
    path('rate/', veiws.professorModuleInstanceScore, name = 'module_instance_score')

]
