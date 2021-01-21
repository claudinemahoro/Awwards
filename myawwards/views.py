from django.http  import HttpResponse,Http404
import datetime as dt 
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Profile, Project, Comment
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
from rest_framework import status

# Create your views here.
def welcome(request):
    projects = Project.objects.all()

    return render(request, 'welcome.html',{"projects":projects})

@login_required(login_url='/accounts/login/')
