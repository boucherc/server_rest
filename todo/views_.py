from rest_framework.response import Response
from rest_framework.views import APIView

from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoList(APIView):

    def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)