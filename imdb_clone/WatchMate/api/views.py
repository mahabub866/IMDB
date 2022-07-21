
from platform import platform
from rest_framework.exceptions import ValidationError

from django.shortcuts import get_object_or_404
from WatchMate.api.permisiion import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from WatchMate.api.serializers import WatchListSerializer,StreamSerializer,ReviewSerializer
from WatchMate.models import WatchList,StreamPlateform,Review
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# from rest_framework import mixins
from rest_framework import generics


# Create your views here.
class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        moive=WatchList.objects.get(pk=pk)
        user=self.request.user
        review_queryset=Review.objects.filter(watchlist=moive,review_user=user)

        if review_queryset.exists():
            raise ValidationError('you have already reviewed this moive ')
        


        if moive.number_rating==0:
            moive.avg_rating=serializer.validated_data['rating']
        else:
            moive.avg_rating=(moive.avg_rating+serializer.validated_data['rating'])/2
        
        moive.number_rating=moive.number_rating+1
        moive.save()


        serializer.save(watchlist=moive,review_user=user)

class ReviewList(generics.ListAPIView):
   
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        return Review.objects.filter(watchlist=pk)

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]


# class ReviewDetails(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
class WatchListAV(APIView):
    permission_classes=[IsAdminOrReadOnly]
    def get(self, request):
        moives = WatchList.objects.all()
        serializer = WatchListSerializer(moives, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchDetailsAV(APIView):
    permission_classes=[IsAdminOrReadOnly]
    def get(self, request,pk):    
        try:
            moive = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'Not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(moive)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        moive = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(moive,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        moive = WatchList.objects.get(pk=pk)
        moive.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StreamPlateformMVS(viewsets.ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]
    queryset = StreamPlateform.objects.all()
    serializer_class = StreamSerializer
    

# class StreamplateformVS(viewsets.Viewsets):
    
#     def list(self, request):
#         queryset = StreamPlateform.objects.all()
#         serializer = StreamSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlateform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamSerializer(watchlist)
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer=StreamSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     def destor(self,request,pk):
#         moive = StreamPlateform.objects.get(pk=pk)
#         moive.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class StreamListAV(APIView):
    permission_classes=[IsAdminOrReadOnly]
    def get(self, request):
        platform = StreamPlateform.objects.all()
        serializer = StreamSerializer(platform, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StreamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamDetailsAV(APIView):
    permission_classes=[IsAdminOrReadOnly]
    def get(self, request,pk):    
        try:
            moive = StreamPlateform.objects.get(pk=pk)
        except StreamPlateform.DoesNotExist:
            return Response({'error':'Not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = StreamSerializer(moive)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        moive = StreamPlateform.objects.get(pk=pk)
        serializer = StreamSerializer(moive,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        moive = StreamPlateform.objects.get(pk=pk)
        moive.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'POST'])
# def moivelist(request):
#     if request.method == 'GET':
#         moives = Moive.objects.all()
#         serializer = MoiveSerializer(moives, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MoiveSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def moive_details(request, pk):
#     if request.method == 'GET':
#         try:
#             moive = Moive.objects.get(pk=pk)
#         except Moive.DoesNotExist:
#             return Response({'error':'Moive not found'},status=status.HTTP_404_NOT_FOUND)
#         serializer = MoiveSerializer(moive)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     if request.method == 'PUT':
#         moive = Moive.objects.get(pk=pk)
#         serializer = MoiveSerializer(moive,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         moive = Moive.objects.get(pk=pk)
#         moive.delete()
#         content = {'please move along': 'nothing to see here'}
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
 