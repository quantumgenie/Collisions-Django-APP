from rest_framework import generics, mixins
from .models import *
from .serializers import *


# API classes used for generating & displaying db content in JSON form and for manipulating the db (POST, GET, PUT, DELETE)

class CollisionDetails(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = Collision.objects.all()
    serializer_class = CollisionSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CollisionList(generics.ListAPIView):
    queryset = Collision.objects.all()
    serializer_class = CollisionSerializer
