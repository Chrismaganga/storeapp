from django.shortcuts import render
from rest_framework import generics
from api.models import Product
from api.serializers import ProductSerializer
# from users.serializers import UserSerializer
# from django.contrib.auth.models import User

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

product_list_create_view = ProductListCreateAPIView.as_view()



class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        return super().perform_update(serializer)


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_content_negotiation(self, request, force=False):
        return super().perform_content_negotiation(request, force)


product_detail_view = ProductDetailAPIView.as_view()

