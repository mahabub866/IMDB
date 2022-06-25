
from django.urls import  path
from WatchMate.api.views import MoiveDetailsAV, MoiveListAV

urlpatterns = [
  
  
    path('list/',MoiveListAV.as_view(),name='moivelist' ),
   
    path('moive_id:<int:pk>/',MoiveDetailsAV.as_view(),name='moive_details' ),
  
]
