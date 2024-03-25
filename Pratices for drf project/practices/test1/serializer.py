from rest_framework import serializers
from django.contrib.auth.models import User
from .models import category, Product
class userAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields= ['first_name','last_name','username','email']

class ProductSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'
    