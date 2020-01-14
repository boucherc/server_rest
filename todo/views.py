import base64
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from todo.models import Todo, Picture
from todo.serializers import TodoSerializer, PictureSerializer


class TodoList(APIView):
    """
    List all todos, or create a new todo.
    """
    def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        errors = {"error":"body must not be empty"}
        if len(request.data) is not 0:
            serializer = PictureSerializer(data=request.data)
            if serializer.is_valid():
                obj = serializer.save()
                encoded = serializer.data.get('img')
                result = open('new2.png', 'wb').write(base64.b64decode(encoded))
                response = Response(serializer.data, status=status.HTTP_201_CREATED)
                # response['Location'] = obj.get_absolute_url()
                return response
            errors = serializer.errors
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):
    """
    Retrieve, update or delete a todo instance.
    """
    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)


    # private
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404


    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PictureView(APIView):

    def get(self, request, format=None):
        todos = Picture.objects.all()
        serializer = PictureSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        errors = {"error":"body must not be empty"}
        if len(request.data) is not 0:
            serializer = PictureSerializer(data=request.data)
            if serializer.is_valid():
                obj = serializer.save()
                encoded = serializer.data.get('img')
                result = open('new2.png', 'wb').write(base64.b64decode(encoded))
                response = Response(status=status.HTTP_201_CREATED)
                # response['Location'] = obj.get_absolute_url()
                return response
            errors = serializer.errors
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

