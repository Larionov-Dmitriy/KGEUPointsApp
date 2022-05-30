from django.urls import path
from .views import *
from .models import *


urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('', login_page, name='login_page'),
    path('profile/', show_profile, name='profile'),
    path('logout/', logout_user, name='logout'),
    path('update/', update_page, name='update'),
    path('rating/', rating_page, name='rate'),
    path('points/', show_points, name='points'),
    path('details/', show_details, name='details'),
]
