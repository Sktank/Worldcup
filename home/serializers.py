__author__ = 'spencertank'


from django.contrib.auth.models import User, Group
from rest_framework import serializers
from home.models import Team, Stadium


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('url', 'id', 'country', 'rank', 'description', 'manager', 'group', 'population')


class StadiumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stadium
        fields = ('url', 'id', 'name', 'city', 'seats', 'latitude', 'longitude', 'image_url')


