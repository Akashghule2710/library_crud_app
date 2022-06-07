from rest_framework import serializers
from .models import BookDetails

class BookDetailsSerializer(serializers.Serializer):
    bno = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    auther = serializers.CharField(max_length=50)
    status = serializers.CharField(max_length=50)

def create(self,data):
    return BookDetails.objects.create(**data) 