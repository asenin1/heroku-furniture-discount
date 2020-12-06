from django.urls import path, include
from accounts.views import redirect_user, register_user, login_user, user_detail

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', redirect_user, name='profile'),
    path('profile/detail/', user_detail, name='user profile'),
    path('signup/', register_user, name='signup'),
    path('registration/login/', login_user, name='login'),
]
