
from django.urls import  path,include
from WatchMate.api.views import  ReviewCreate, StreamDetailsAV,ReviewDetails, StreamListAV,StreamPlateformMVS, UserReview, WatchDetailsAV,WatchListAV,ReviewList

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlateformMVS,basename='stream')
   
urlpatterns = [
  
  
    path('watchlist/',WatchListAV.as_view(),name='moivelist' ),
    path('',include(router.urls)),
    # path('api-auth/',include('rest_framework.urls')),
   
    # path('watchlist/moive_id:<int:pk>/',WatchDetailsAV.as_view(),name='moive_details' ),
    #path('streamlist/',StreamListAV.as_view(),name='streamlist' ),
    #path('streamlist/moive_id:<int:pk>/',StreamDetailsAV.as_view(),name='stream_details' ),
    
   
    # path('reviewlist/review_id:<int:pk>/',ReviewDetails.as_view(),name='reviewdetails' ),

    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='reviewcreate' ),
    path('<int:pk>/review/',ReviewList.as_view(),name='reviewlist' ),
    path('review/review_id:<int:pk>/',ReviewDetails.as_view(),name='reviewdetails' ),
    # path('reviews/username:<str:username>/',UserReview.as_view(),name='user-review-details' ),
    path('reviews/',UserReview.as_view(),name='user-review-details' ),
  
]
 