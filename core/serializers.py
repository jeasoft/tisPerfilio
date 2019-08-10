from rest_framework import serializers
from core.models import User, Experience, Education, Certification

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ("username","first_name","last_name")
