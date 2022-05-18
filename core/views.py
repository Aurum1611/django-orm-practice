from rest_framework import viewsets
from .models import UserProfile, College, State, City
from .serializers import UserProfileSerializer, CollegeSerializer, \
    CitySerializer, StateSerializer
from django.db.models import Q


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    
    def get_queryset(self):
        addr = self.request.query_params.get('address')
        name = self.request.query_params.get('name')
        
        if addr:
            users = UserProfile.objects.filter(address__contains=addr)
        elif name:
            users = UserProfile.objects.filter(
                Q(name__startswith=name) | Q(name__endswith=name)
            )
        else:
            users = UserProfile.objects.order_by('-dob')
        return users


class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = CitySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = StateSerializer
