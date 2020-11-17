from rest_framework.generics import get_object_or_404
from rest_framework import generics, mixins

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import permissions

from .models import Curso, Rating
from .serializers import CursoSerializer, RatingSerializer
from .permissions import SuperUser

"""
API V1
"""


class CursosAPIView(generics.ListCreateAPIView):
    permission_classes = (
        SuperUser,
        permissions.DjangoModelPermissions, )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class RatingsAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()
    # kwargs pega o queryparams /2/ nesse caso curso_pk


class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                  curso_id=self.kwargs.get('curso_pk'),
                                  pk=self.kwargs.get('rating_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('rating_pk'))


"""
API V2
"""


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def ratings(self, request, pk=None):
        self.pagination_class.page_size = 1
        ratings = Rating.objects.filter(curso_id=pk)
        page = self.paginate_queryset(ratings)

        if page is not None:
            serializer = RatingSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

"""
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
"""


class RatingViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
   # mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
