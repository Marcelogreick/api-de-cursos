# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Rating
from .serializers import CursoSerializer, RatingSerializer


class CursoAPIView(APIView):
    """
    Api
    """

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, resquest):
        serializer = CursoSerializer(data=resquest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        ## return Response({"id": serializer.data['id'], "curso": serializer.data['title']}, status=status.HTTP_201_CREATED)


class RatingAPIView(APIView):
    """
    Api
    """

    def get(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

    def post(self, resquest):
        serializer = RatingSerializer(data=resquest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


