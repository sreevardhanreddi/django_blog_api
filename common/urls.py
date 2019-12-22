from django.urls import path
from common.views import *

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register_user'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
]
