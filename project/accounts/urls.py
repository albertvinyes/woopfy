from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.RegularUserList.as_view()),
    path('<int:pk>/', views.RegularUserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
