from django.urls import path
from users.views import *

urlpatterns = [
    path('', UserList.as_view()),
    path('user/<int:user_id>/', UserList.as_view()),
    path('user/<int:user_id>/', UserDetail.as_view())
    ]