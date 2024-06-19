from django.urls import path, include
from rest_framework.routers import DefaultRouter
from wanderellaapi.views import register_user, login_user
from wanderellaapi.views import FlightView, AirlineView, RentalCarView

router = DefaultRouter(trailing_slash=False)
router.register(r'flights', FlightView, 'flight')
router.register(r'airlines', AirlineView, 'airline')
router.register(r'cars', RentalCarView, 'car')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
]