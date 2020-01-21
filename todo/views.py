import base64
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from todo.models import Picture
from todo.serializers import PictureSerializer


class LookForIt(APIView):
    """
    List all todos, or create a new todo.
    """

    def get(self, request, format=None):
        todos = Picture.objects.all()
        serializer = PictureSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Pictures(APIView):
    """
    Retrieve, update or delete a todo instance.
    """

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = PictureSerializer(todo)
        return Response(serializer.data)

    # private
    def get_object(self, pk):
        try:
            return Picture.objects.get(pk=pk)
        except Picture.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = PictureSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
