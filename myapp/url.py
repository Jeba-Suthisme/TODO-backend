from django.urls import path
from .views import create_chocolate,update_chocolate,delete_chocolate,chocolate_list,create_user,login_user,get_user,mailSend

urlpatterns=[

    # todo
    path('createchoco/',create_chocolate,name='create_chocolate'),
    # path('get/',get_chocolate,name='get_chocolate'),
    path('update/<int:pk>/',update_chocolate,name='update_chocolate'),
    
    path('delete/<int:pk>/',delete_chocolate,name='delete_chocolate'),
    path('getlist/',chocolate_list,name='chocolate_list'),

    # login

    path('createuser/',create_user,name='create_user'),
    path('login/',login_user,name='login_user'),
    path('get/',get_user,name='get_user'),

    # email
    path('contact/',mailSend,name='sendmail')



]