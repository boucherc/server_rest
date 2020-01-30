import base64
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from CNN import query_online
from todo.models import Picture, Result
from todo.serializers import PictureSerializer, ResultSerializer


def get_object(pk):
    try:
        return Picture.objects.get(pk=pk)
    except Picture.DoesNotExist:
        raise Http404


class LookForIt(APIView):
    """
    List all todos, or create a new todo.
    """

    def get(self, request, pk, format=None):
        obj = get_object(pk)
        url = "./media/"+str(getattr(obj, 'img'))
        print(url)
        res = query_online.getMatches(url)
        todos = Picture.objects.all()
        query = set()
        for i in range(0,len(res)):
            print(res[i][0], res[i][1])
            query.add(Result.objects.create(url=res[i][0], score=res[i][1]).pk)
        list = Result.objects.filter(pk__in = query)
        serializer = ResultSerializer(list, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = PictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Pictures(APIView):
#     """
#     Retrieve, update or delete a todo instance.
#     """
#
#     def get(self, request, format=None):
#         todos = Picture.objects.all()
#         serializer = PictureSerializer(todos, many=True)
#         return Response(serializer.data)
#
#     # private
#     def get_object(self, pk):
#         try:
#             return Picture.objects.get(pk=pk)
#         except Picture.DoesNotExist:
#             raise Http404
#
#     def delete(self, request, pk, format=None):
#         todo = self.get_object(pk)
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def put(self, request, pk, format=None):
#         todo = self.get_object(pk)
#         serializer = PictureSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
