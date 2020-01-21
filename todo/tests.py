from django.test import TestCase

from todo.models import Picture

# Create some instances
todo1 = Picture(description="faire les courses", priority="high")
todo1.save()
todo2 = Picture(description="aller à la plage")
todo2.save()

todos = Picture.objects.all()
for todo in todos:
    print("%d %s" % (todo.id, todo.description))

todos = Picture.objects.filter(priority="low")

todo1.delete()


# serialization

from todo.serializers import PictureSerializer
serializer = PictureSerializer(todo2)

from rest_framework.renderers import JSONRenderer
content = JSONRenderer().render(serializer.data)


serializer.data
#   python native data type
#  {'id': 1, 'description': 'Faire les courses', 'deadline': '2018-10-12T03:31:38.913422Z', 'done': False, 'priority': 'normal', 'tags': 'g1 g2'}

from rest_framework.renderers import JSONRenderer
content = JSONRenderer().render(serializer.data)

# b'{"id":1,"description":"Faire les courses","deadline":"2018-10-12T03:31:38.913422Z","done":false,"priority":"normal","tags":"g1 g2"}'
