from rest_framework import serializers
from . import models

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.List
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class ListProductsSerializer(serializers.ModelSerializer):

    List = ListSerializer()
    Product = ProductSerializer()
    class Meta:
        model = models.ListProducts 
        fields = '__all__'