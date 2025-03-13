from django.test import TestCase

from main.models import Listing
import uuid

uuid_id = uuid.UUID("f0de53e8-8341-4e92-bc94-4e654f4f0372")  # Use the UUID from your error
listing = Listing.objects.filter(id=uuid_id).first()

print("Listing Found:", listing)
