"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import urls as myapp_urls
from myapp.class_based_views import CourseList, AddCourse, UpdateCourse, DeleteCourse
from myapp import viewset_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("myapp/", include(myapp_urls)),
    path("course-list/", CourseList.as_view()),
    path("add-course/", AddCourse.as_view()),
    path("update-course/<int:pk>/", UpdateCourse.as_view()),
    path("delete-course/<int:pk>/", DeleteCourse.as_view()),
    path("", include(viewset_urls)),
]
