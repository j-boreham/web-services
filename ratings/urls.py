
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [

    path('',views.home, name = 'home'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('listModules/', views.listModules.as_view(), name='modules'),
    path('login/',views.login.as_view(), name = 'login'),
    # path('logout/',views.logout,name='logout'),
    path('register/',views.register.as_view(), name='register'),
    # path('viewProfs/',views.viewProfessors, name='professors'),
    # path('profModule/', views.professorModuleScore,name=' professor_module_score'),
    # path('rate/', veiws.professorModuleInstanceScore, name = 'module_instance_score')

]
