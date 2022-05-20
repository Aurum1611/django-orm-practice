from rest_framework import viewsets
from .models import UserProfile, College, State, City
from .serializers import UserProfileSerializer, CollegeSerializer, \
    CitySerializer, StateSerializer
from django.db.models import Q, F
from rest_framework.response import Response
from rest_framework.decorators import action


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

    @action(detail=False)
    def age_filter(self, req, **kwargs):
        age_max = req.query_params.get('age_max')
        age_min = req.query_params.get('age_min')

        if age_max and age_min:
            users = UserProfile.objects.filter(
                Q(age__gte=age_min) & Q(age__lt=age_max)
            ).order_by('dob')
            serializer = UserProfileSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'parameters not recieved'})


class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = CitySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = StateSerializer
