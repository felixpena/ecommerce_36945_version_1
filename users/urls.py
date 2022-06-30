from django.urls import path
from users.views import Update_user_profile


urlpatterns =[
    path('update-user-profile/<int:pk>/', Update_user_profile.as_view(), name = 'update_user_profile'),
    ]

