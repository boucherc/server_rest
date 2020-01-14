from rest_framework import serializers

from todo.models import Todo, Picture


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id', 'description', 'deadline', 'done', 'priority', 'tags')

class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ('name', 'img')

# class TodoInputSerializer(serializers.Serializer):
#     description = serializers.CharField()
#     deadline = serializers.DateField()
#     done = serializers.
#
#     keywords = serializers.ListField(
#         child=serializers.CharField(max_length=40, min_length=1, allow_blank=False, trim_whitespace=True),
#         min_length=1, max_length=5
#     )
#     categories = serializers.ListField(
#         required=False,
#         child=serializers.CharField(max_length=60, min_length=7, allow_blank=False, trim_whitespace=True),
#         min_length=1, max_length=5
#     )
#     scope = serializers.ChoiceField(choices=['public', 'private'])
#     levels = serializers.MultipleChoiceField(required=False, choices=['A1','A2','B1','B2','C1','C2'])
#     sort = serializers.ChoiceField(choices=['score','date'], required=False)