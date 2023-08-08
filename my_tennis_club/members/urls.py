from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('main', views.main, name= 'main'),
    path('testing', views.testing, name='template'),
    # path('erro_', views.error_404, name='error_404'), no url for error_404 page is required
    path('members', views.mymembers, name='mymembers'),
    path('members/details/<int:id>', views.member_details, name='member_details')
]