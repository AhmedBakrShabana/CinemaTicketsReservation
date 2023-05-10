from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest,Reservation,Movie
from rest_framework.decorators import api_view
from .serializers import GuestSerializer,ReservationSerializer,MovieSerializer
from rest_framework import status,filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.
def no_rest_no_model(request):
    
    guests = [
        {
            'id':1,
            'name':'Ahmed',
            'mobile': '01122212104'

        },
        {
            'id':2,
            'name':'Bakr',
            'mobile':'01554246441'

        }
    ]
    return JsonResponse(guests,safe=False)

def no_rest_from_model(request):
    data = Guest.objects.all()

    response = {
        'Guests': list(data.values('name','mobile'))
    }
    return JsonResponse(response)

@api_view(['GET','POST'])

def fbv_list(request):

    if request.method == 'GET':
        Guests = Guest.objects.all()
        serializer = GuestSerializer(Guests,many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])

def fbv_pk(request,pk):
    try:
        guest = Guest.objects.get(pk = pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CBV_LIST(APIView):
    def get(self,request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_401_UNAUTHORIZED)
    

class CVB_PK(APIView):
    
    def get_object(self,pk):
        try:
            return Guest.objects.get(pk = pk)
        except Guest.DoesNotExist:
            raise Http404
    