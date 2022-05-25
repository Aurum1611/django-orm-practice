from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import UserProfileViewSet, CollegeViewSet, \
    CityViewSet, StateViewSet, ElectiveViewSet

router = routers.DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet, basename='userprofiles')
router.register(r'colleges', CollegeViewSet)
router.register(r'cities', CityViewSet)
router.register(r'states', StateViewSet)
router.register(r'electives', ElectiveViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
