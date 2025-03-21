from django.urls import path
from main.views import landing_view, home_view, list_view, listing_view, edit_view, like_listing_view, inquire_listing_view
import uuid

urlpatterns = [
    path('', landing_view, name= 'main'),
    path('home/', home_view, name='home'),
    path('list/', list_view, name='list'),
    path('listing/<str:id>/', listing_view, name='listing'),
    path('listing/<str:id>/edit/', edit_view, name='edit'),
    path('listing/<str:id>/like/', like_listing_view, name='like_listing'),
    path('listing/<str:id>/inquire/', inquire_listing_view, name='inquire_listing'),
]