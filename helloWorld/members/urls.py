
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.main, name='main'), # Main.html index file
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.memberdetails, name='memberdetails'),
    path('testing/', views.testing, name='testing'),

    
    #path('add_member/', views.add_member, name='add_member')
]