from rest_framework import serializers
from .models import *

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model=BooksModel
        fields='__all__'