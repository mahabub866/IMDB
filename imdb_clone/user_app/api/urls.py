from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path,include

from user_app.api.views import logout_view, registation_view

urlpatterns = [
    path('login/', obtain_auth_token,name='login'),
    path('registration/', registation_view,name='registration'),
    path('logout/', logout_view,name='logout'),
   
]