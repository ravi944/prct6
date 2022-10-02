from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

## Function based views
from rest_framework import status
from rest_framework import viewsets


from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def Booklist(request):
    booksobj = BooksModel.objects.all()
    serializer = Bookserializer(booksobj, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_Book(request):
    booksobj = BooksModel.objects.all()
    serializer = Bookserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


######
@api_view(['POST'])
def update_Book(request, id):
    booksobj = BooksModel.objects.get(id=id)
    serializer = Bookserializer(instance=booksobj, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_Book(request, id):
    booksobj = BooksModel.objects.get(id=id)
    booksobj.delete()
    return Response("deleted successfully")



class Studentviewset(viewsets.ModelViewSet):
    queryset = BooksModel.objects.all()
    serializer_class = Bookserializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
