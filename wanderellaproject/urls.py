from django.urls import path, include
from rest_framework.routers import DefaultRouter
from wanderellaapi.views import register_user, login_user

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
]