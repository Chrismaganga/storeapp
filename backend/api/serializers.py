from rest_framework import serializers
from api.models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
         
            'user',
            'title',
            'content',
            'image',
            'price',
            'sale_price',
            'my_discount'
            
        ]


    def get_my_discount(self,obj):
        try:
            return obj.get_discount()
        except:
            return None
