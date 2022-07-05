
from django.urls import  path
from WatchMate.api.views import  StreamDetailsAV, StreamListAV, WatchDetailsAV,WatchListAV


urlpatterns = [
  
  
    path('watchlist/',WatchListAV.as_view(),name='moivelist' ),
   
    path('watchlist/moive_id:<int:pk>/',WatchDetailsAV.as_view(),name='moive_details' ),
    path('streamlist/',StreamListAV.as_view(),name='streamlist' ),
    path('streamlist/moive_id:<int:pk>/',StreamDetailsAV.as_view(),name='stream_details' ),
  
]
