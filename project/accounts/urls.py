#from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import include, path
from accounts import views

urlpatterns = [
    path('', views.RegularUserList.as_view()),
    path('<int:pk>/', views.RegularUserDetail.as_view()),
    path('login/', views.login_view),
#    path('logout/', views.logout_view),
#    path('rest-auth/', include('rest_auth.urls')),
    path('test/login/', views.test_login),
    path('test/index/', views.test_index),
]

urlpatterns = format_suffix_patterns(urlpatterns)
