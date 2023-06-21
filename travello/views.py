from django.shortcuts import render
from .models import Destination
from django.http import JsonResponse
from .serializers import DestinationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):

    # Instead of creating separate objects for Destination class, we want to get it from database. So to do that we do the following code.
    
    dests = Destination.objects.all(); 

    # dest1 = Destination()
    # dest1.name = 'MUMBAI'
    # dest1.price = 700
    # dest1.id = 1
    # dest1.img = 'destination_1.jpg'
    # dest1.desc = 'The city that never sleeps.'
    # dest1.offer = True

    # dest2 = Destination()
    # dest2.name = 'JAIPUR'
    # dest2.price = 800
    # dest2.id = 2
    # dest2.img = 'destination_2.jpg'
    # dest2.desc = 'The pink city.'
    # dest2.offer = False

    # dest3 = Destination()
    # dest3.name = 'BANGALORE'
    # dest3.price = 900
    # dest3.id = 3
    # dest3.img = 'destination_3.jpg'
    # dest3.desc = 'The Green city.'
    # dest3.offer = True

    # # return render(request, 'index.html',{'dest1': dest1,  'dest2' : dest2,'dest3' : dest3 })
    # # instead of passing each object separately to index.html we can pass the list of objects

    # dests = [dest1, dest2, dest3]
    return render(request, 'index.html',{'dests': dests}) 
    
# Serializers for Api

@api_view(['GET','POST'])
def destination_list(request, format=None):
    
    if request.method == 'GET':
        # get all the destinations
        destinations = Destination.objects.all()

        # serialize the destinations
        serializer = DestinationSerializer(destinations, many = True)

        # return json response
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DestinationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def destination_detail(request, id, format = None):
    try :
        destination = Destination.objects.get(pk = id)
    except Destination.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
       serializer =  DestinationSerializer(destination)
       return Response(serializer.data)

    if request.method == 'PUT':
       serializer =  DestinationSerializer(destination, data = request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
       return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        destination.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
