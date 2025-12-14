from django.shortcuts import render
from django.http import HttpResponse


def home(Request):
    return HttpResponse("I think therefore I am")
