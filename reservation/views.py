from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.request import Request

from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer, userSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})


class menuview(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class singleitemview(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
    
    

class bookingview (viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = bookingSerializer
    


class userview (viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = userSerializer
   permission_classes = [permissions.IsAuthenticated]




# class bookingview(viewsets.ModelViewSet):
#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = bookingSerializer(items, many =True)
#         return Response (serializer.data)
    
#     def post (self, request):
#         serializer =bookingSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response ({"status": "sucess", "data": serializer.data})



    
 
    
    
    
    
    
    # def get(self, request):
    #     items = Menu.objects.all()
    #     serializer = menuSerializer(items, many =True)
    #     return Response (serializer.data)

    # def post (self, request):
    #     serializer =menuSerializer(data=request.data)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status": "success", "data": serializer.data})
    #     else:
    #         return Response(serializer.errors, status=400)  # 400 Bad Request


    # def delete (self, request):
    #     serializer =menuSerializer(data=request.data)
        
    #     if serializer.is_valid():
    #         serializer.delete()
    #         return Response({"status": "success", "data": serializer.data})
    #     else:
    #         return Response(serializer.errors, status=400)  # 400 Bad Request

# def reservation(request):
#     return HttpResponse("Thank you for your reservation")


def index (request):
    return render (request, 'index.html', {})