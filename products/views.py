import random

from rest_framework import viewsets, status
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Products, User
from products.serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):

    def list(self,request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)

    def retrive(self, request, pk=None):
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(instance=product,
                                       data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Products.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
