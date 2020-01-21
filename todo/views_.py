from rest_framework.response import Response
from rest_framework.views import APIView

from todo.models import Picture
from todo.serializers import PictureSerializer


class TodoList(APIView):

    def get(self, request, format=None):
        todos = Picture.objects.all()
        serializer = PictureSerializer(todos, many=True)
        return Response(serializer.data)