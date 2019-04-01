from . import models
from . import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics, status

# Create your views here.
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        serializer = serializers.ProductSerializer(
            products, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = models.Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.ProductSerializer(product, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.ProductSerializer(
            product, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        models.product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class add_products_to_lists(generics.ListCreateAPIView):
    queryset = models.ListProducts.objects.all()
    serializer_class = serializers.ListProductsSerializer

class create_list(generics.CreateAPIView):
    queryset = models.List.objects.all()
    serializer_class = serializers.ListSerializer

class list(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.List.objects.all()
    serializer_class = serializers.ListSerializer

class lists(generics.ListCreateAPIView):
    queryset = models.List.objects.all()
    serializer_class = serializers.ListSerializer