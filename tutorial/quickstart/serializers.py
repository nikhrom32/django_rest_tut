from django.contrib.auth.models import User, Group
from rest_framework import serializers


# Hyperlinked relations, PK and anything else works as well, but this one is a RESTful design

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
