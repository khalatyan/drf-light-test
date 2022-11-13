from django.db import transaction

import json
from rest_framework import serializers
from rest_framework.utils import model_meta
from rest_framework.serializers import SerializerMethodField

from core.models import Division, Post, Employee


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Employee
        fields = "__all__"


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class DivisionSerializer(serializers.ModelSerializer):
    division_employee = EmployeeSerializer(many=True)
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Division
        fields = "__all__"