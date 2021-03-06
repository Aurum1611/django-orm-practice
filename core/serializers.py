from rest_framework import serializers
from .models import State, City, College, UserProfile, ElectiveSubject


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'dob', 'email', 'phone_num', 'user', 
                  'address', 'city', 'state', 'college', 'age', 'elective')


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'name', 'address', 'phone_num', 'city', 'state')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'code', 'state')


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'name', 'code')


class ElectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectiveSubject
        fields = ('id', 'name')
