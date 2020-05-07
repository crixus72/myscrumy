#Django
from django.http import HttpResponse
from django.shortcuts import render


def get_grading_parameters(request):
    return HttpResponse("Welcome to Django")


# Create your views here.
