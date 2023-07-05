from rest_framework import serializers
from rest_framework.serializers import ValidationError
from todo.models import Task
from django.contrib.auth.models import User


class User_S(serializers.RelatedField):
    def to_representation(self, value):
        return f"{value.username}"
    
    def to_internal_value(self, data):
        try:
            username=User.objects.get(username=data)
            return username
        except:
            raise ValidationError("this username does not exist")
        
class Do_S(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=["id","title","description","completed","created_at"]
        
