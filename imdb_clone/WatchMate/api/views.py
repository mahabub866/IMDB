
from WatchMate.api.serializers import WatchListSerializer
from WatchMate.models import WatchList
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class WatchListAV(APIView):
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

class MoiveDetailsAV(APIView):
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
    
 