from django.test import TestCase

# Create your tests here.

from My_Application.models import event_request

new_event = event_request(
    organizer_name="John Doe",  # Organizer's name
    department="Computer Science",  # Department name
    mobile_no="1234567890",  # Organizer's contact number
    from_date="2024-12-01",  # Event start date
    to_date="2024-12-02",  # Event end date
    from_time="10:00:00",  # Event start time (24-hour format)
    to_time="15:00:00",  # Event end time (24-hour format)
    expected_participants=150,  # Number of expected participants
    internals=100,  # Number of internal participants
    externals=50,  # Number of external participants
    no_of_guests=2,  # Number of guests
    guest_name="Dr. Alice, Dr. Bob",  # Guest names (comma-separated if multiple)
    guest_designation="Professor, Associate Professor",  # Guest designations
    guest_org="University of X, Institute of Y",  # Guest organizations
    financial_required=True,  # True if financial assistance is required
    reward_points=False,  # False if reward points are not required
    on_duty_required=True,  # True if on-duty is required
    venue_required=True,  # True if a venue is required
    photography_required=False,  # False if photography is not required
    accessories_required=True,  # True if accessories are required
    vehicle_required=False,  # False if a vehicle is not required
    acc_required=True,  # True if accommodation is required
    other_requirements="Projector, Mic",  # Any additional requirements
)
new_event.save()
