from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Items, Category
from .serializer import ItemSerializer, CategorySerializer

# Create your views here.
class ItemHandling(APIView):
    def get(self, request):
        allItems = Items.objects.all()
        serializer = ItemSerializer(allItems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        new_item = {
            'identifier': request.data.get('identifier'),
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'description': request.data.get('description'),
            # 'category': request.data.get('category'),
            # 'image': request.data.get('image')
        }
        serializer = ItemSerializer(data = new_item)
        print(serializer)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else: 
            return Response(new_item, status = status.HTTP_400_BAD_REQUEST)
        

class CategoryHandling(APIView):
    def get(self, request, category):
        category_items = Category.objects.filter(category = category)
        serializer = CategorySerializer(category_items, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request, category):
        new_category = {
            "category": request.data.get('category'),
            "description": request.data.get('description')
        }
        serializer = CategorySerializer(data = new_category)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)    

        