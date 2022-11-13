from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.core.exceptions import PermissionDenied

from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Division, Post, Employee
from core.serializers import DivisionSerializer


class DivisionViewSet(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    serializer_class = DivisionSerializer

    def get(self, request):
        queryset = Division.objects.filter(parent=None)
        return Response({
            'divisions': queryset
        })
