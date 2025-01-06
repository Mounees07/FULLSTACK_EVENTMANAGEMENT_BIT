from django.db import models
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    class Meta:
        db_table = 'user'
    def __str__(self):
        return self.username
class Event(models.Model):
    organizer_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    task_id=models.CharField(max_length=15)
    event_name=models.CharField(max_length=15)
    from_date = models.DateField()
    to_date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    expected_participants = models.IntegerField()
    internals = models.IntegerField()
    externals = models.IntegerField()
    no_of_guests = models.IntegerField()
    guest_name = models.CharField(max_length=200)
    guest_designation = models.CharField(max_length=100)
    guest_org = models.CharField(max_length=200)
    financial_required = models.BooleanField(default=False)
    reward_points = models.BooleanField(default=False)
    on_duty_required = models.BooleanField(default=False)
    venue_required = models.BooleanField(default=False)
    photography_required = models.BooleanField(default=False)
    accessories_required = models.BooleanField(default=False)
    vehicle_required = models.BooleanField(default=False)
    acc_required = models.BooleanField(default=False)
    other_requirements = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approval_status = models.CharField(
        max_length=10,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending'
    )
    admin_comments = models.TextField(blank=True, null=True)
    class Meta:
        db_table = 'Event'  # Custom table name

    def __str__(self):
        return f"{self.organizer_name} ({self.department})"



class VenueRequest(models.Model):
    task_id = models.CharField(max_length=100)
    no_of_venues = models.IntegerField()
    audio_requirements = models.TextField(blank=True, null=True)
    venue_types = models.TextField()  # Store as a comma-separated string
    hall_requirements = models.TextField(blank=True, null=True)
    expected_internet = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'VenueRequest'  # Custom table nam
    def __str__(self):
        return f"Task ID: {self.task_id}"



class PhotographyRequest(models.Model):
    task_id = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    requirements = models.TextField(blank=True, null=True)
    services = models.TextField(blank=True, null=True)
    preferred_time = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        db_table = 'PhotographyRequest'  # Custom table nam
    def __str__(self):
        return f"Task ID: {self.task_id}"


class AccessoriesRequest(models.Model):
    task_id = models.CharField(max_length=255)
    venue_name = models.CharField(max_length=255)
    large_memento = models.IntegerField(default=0)
    small_memento = models.IntegerField(default=0)
    shawl = models.IntegerField(default=0)
    water_bottles = models.IntegerField(default=0)
    pen_pencil = models.IntegerField(default=0)
    scribbling_pad = models.IntegerField(default=0)
    other_requirements = models.TextField(blank=True, null=True)
    class Meta:
        db_table = 'AccessoriesRequest'  # Custom table nam
    def __str__(self):
        return f"Task ID: {self.task_id}"


class VehicleRequest(models.Model):
    task_id = models.CharField(max_length=255)
    no_of_vehicles = models.IntegerField()
    purpose_of_visit = models.TextField(blank=True, null=True)
    vehicle_types = models.TextField(blank=True, null=True)
    special_requirements = models.TextField(blank=True, null=True)
    class Meta:
        db_table = 'VehicleRequest'  # Custom table nam
    def __str__(self):
        return f"Task ID: {self.task_id}"


class AccommodationRequest(models.Model):
    task_id = models.CharField(max_length=255)
    no_of_participants = models.IntegerField()
    no_of_guests = models.IntegerField(blank=True, null=True)
    ACCOMMODATION_TYPE_CHOICES = [
        ('single-room', 'Single Room'),
        ('double-room', 'Double Room'),
        ('suite', 'Suite'),
        ('shared', 'Shared'),
    ]
    accommodation_type = models.CharField(max_length=20, choices=ACCOMMODATION_TYPE_CHOICES)
    special_requirements = models.TextField(blank=True, null=True)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    class Meta:
        db_table = 'AccommodationRequest'  # Custom table nam
    def __str__(self):
        return f"Task ID: {self.task_id}"
    
   #Admin 
