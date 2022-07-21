from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path, include

from user_app.api.views import logout_view, registation_view,LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('registration/', registation_view, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('logoutjwt/', LogoutView.as_view(), name='logoutjwt'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
