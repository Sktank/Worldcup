# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from bs4 import BeautifulSoup, SoupStrainer
import urllib2
from bs4.element import Tag, NavigableString
import re
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User, Group
from home.models import Team, Stadium
from rest_framework import viewsets
from home.serializers import UserSerializer, GroupSerializer, TeamSerializer, StadiumSerializer

def base(request, template="home/content.html"):
    return render_to_response(template)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class StadiumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
