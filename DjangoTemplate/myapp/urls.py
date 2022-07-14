from django.urls import path
from .views  import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact,  name='contact'),
    path('login/', login_user,  name='login'),
    path('logout/',logout_user,  name='logout_'),
    path('register/',register_user, name='register_'),

]