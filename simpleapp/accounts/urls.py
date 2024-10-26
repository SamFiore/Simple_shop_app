from django.urls import path
from .views import SingUpView,LoginUpView

urlpatterns = [
    path('singup/',SingUpView.as_view(),name='singup'),
    path('login/',LoginUpView.as_view(),name='login')
]