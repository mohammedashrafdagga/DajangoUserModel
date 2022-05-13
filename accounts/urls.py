from django.urls import path
from . import views as vs


urlpatterns = [
    path('singup/', vs.registerUser, name='singup'),
    path('profile/', vs.profile, name='profile'),
    path('edit-profile/', vs.profile_edit, name='edit-profile')
]
