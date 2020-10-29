from django.shortcuts import render, HttpResponse


def create(request):
  return render(request, HttpResponse('hellow'))
