from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.viewset_example import StudentViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'student-list', StudentViewSet,basename="student-list")
router.register(r'student-update/<int:pk>', StudentViewSet,basename="student-update")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]