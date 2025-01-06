from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404,redirect

from .models import Event, VenueRequest, PhotographyRequest, AccessoriesRequest, VehicleRequest, AccommodationRequest
from .models import Event
from .models import VenueRequest
from .models import PhotographyRequest
from .models import AccessoriesRequest
from .models import VehicleRequest
from .models import AccommodationRequest
from .models import User
import json
import logging

# Set up logging
logger = logging.getLogger(__name__)

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            confirm_password = data.get("confirm_password")

            if password != confirm_password:
                return JsonResponse({"status": "error", "message": "Passwords do not match!"})

            if User.objects.filter(username=username).exists():
                return JsonResponse({"status": "error", "message": "Username already exists!"})

            if User.objects.filter(email=email).exists():
                return JsonResponse({"status": "error", "message": "Email already exists!"})

            hashed_password = make_password(password)  # Hash password before saving
            User.objects.create(username=username, email=email, password=hashed_password)

            return JsonResponse({"status": "success", "message": "User registered successfully!"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request method"})
        
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            user = User.objects.filter(email=email).first()

            if not user:
                return JsonResponse({"status": "error", "message": "Invalid email or password!"})

            # Check if the password matches using Django's check_password method
            if check_password(password, user.password):
                return JsonResponse({"status": "success", "message": "Login successful!"})
            else:
                return JsonResponse({"status": "error", "message": "Invalid email or password!"})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request method"})

ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "admin123"  # In a real-world application, never store passwords in plain text!

def admin_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            # Compare with hardcoded credentials
            if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
                return JsonResponse({"status": "success", "message": "Login successful!"})
            else:
                return JsonResponse({"status": "error", "message": "Invalid credentials."})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request method"})

# View to handle event request submission
@csrf_exempt  # Remove this in production if CSRF tokens are properly set up in templates
def submit_event_request(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Check for missing required fields
            required_fields = ['organizer_name', 'department', 'mobile_no']
            missing_fields = [field for field in required_fields if not data.get(field)]
            if missing_fields:
                return JsonResponse(
                    {'status': 'error', 'message': f'Missing fields: {", ".join(missing_fields)}'}, 
                    status=400
                )
            
            # Save event data
            Events = Event(
                organizer_name=data.get('organizer_name'),
                department=data.get('department'),
                mobile_no=data.get('mobile_no'),
                task_id=data.get('task_id'),
                event_name=data.get('event_name'),
                from_date=data.get('from_date'),
                to_date=data.get('to_date'),
                from_time=data.get('from_time'),
                to_time=data.get('to_time'),
                expected_participants=data.get('expected_participants'),
                internals=data.get('internals'),
                externals=data.get('externals'),
                no_of_guests=data.get('no_of_guests'),
                guest_name=data.get('guest_name'),
                guest_designation=data.get('guest_designation'),
                guest_org=data.get('guest_org'),
                financial_required=data.get('financial_required') == 'yes',
                reward_points=data.get('reward_points') == 'yes',
                on_duty_required=data.get('on_duty_required') == 'yes',
                venue_required=data.get('venue_required') == 'yes',
                photography_required=data.get('photography_required') == 'yes',
                accessories_required=data.get('accessories_required') == 'yes',
                vehicle_required=data.get('vehicle_required') == 'yes',
                acc_required=data.get('accommodation_required') == 'yes',
                other_requirements=data.get('other_requirements')
            )
            Events.save()
            return JsonResponse({'status': 'success', 'message': 'Event data saved successfully!'})
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            logger.error(f"Error while saving event data: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)


@csrf_exempt 
def submit_venue_form(request):
    if request.method == 'POST':
        try:
            if not request.body:
                return JsonResponse({'success': False, 'message': 'Empty request body'}, status=400)
            
            data = json.loads(request.body)
            print("Parsed data:", data)  # Log the parsed data for debugging
            venue = VenueRequest(
                task_id=data.get('task_id'),
                no_of_venues=data.get('no_of_venues'),
                audio_requirements=data.get('audio_requirements'),
                venue_types=data.get('venue_types'),
                hall_requirements=data.get('hall_requirements'),
                expected_internet=data.get('expected_internet'),
            )
            venue.save()
            return JsonResponse({'success': True, 'message': 'Form submitted successfully!'})
        except json.JSONDecodeError as e:
            return JsonResponse({'success': False, 'message': f'Invalid JSON: {e}'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error: {e}'}, status=500)
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405) 


@csrf_exempt
def submit_photography_form(request):
    """
 
    """
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body)
            photography=PhotographyRequest(
            # Validate and retrieve fields from the data
            task_id = data.get('task_id'),
            venue = data.get('venue_name'),
            requirements = data.get('requirements', ''),
            services = ', '.join(data.get('services', [])), # Combine services into a single string
            preferred_time = data.get('preferred_time', ''))
            photography.save()

          
            # Assuming `EventType` exists and is related to `PhotographyRequest`
       

            return JsonResponse({'success': True, 'message': 'Photography Request submitted successfully.'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data.'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'An error occurred: {str(e)}'}, status=500)
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def submit_accessories_form(request):
    if request.method == 'POST':
        try:
            if not request.body:
                return JsonResponse({'success': False, 'message': 'Empty request body'}, status=400)
            
            data = json.loads(request.body)
            accessories_request = AccessoriesRequest(
                task_id=data.get('task_id'),
                venue_name=data.get('venue_name'),
                large_memento=data.get('large_memento', 0),
                small_memento=data.get('small_memento', 0),
                shawl=data.get('shawl', 0),
                water_bottles=data.get('water_bottles', 0),
                pen_pencil=data.get('pen_pencil', 0),
                scribbling_pad=data.get('scribbling_pad', 0),
                other_requirements=data.get('other_requirements'),
            )
            accessories_request.save()
            return JsonResponse({'success': True, 'message': 'Form submitted successfully!'})
        except json.JSONDecodeError as e:
            return JsonResponse({'success': False, 'message': f'Invalid JSON: {e}'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error: {e}'}, status=500)
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def submit_vehicle_form(request):
    if request.method == 'POST':
        try:
            if not request.body:
                return JsonResponse({'success': False, 'message': 'Empty request body'}, status=400)
            
            data = json.loads(request.body)
            vehicle_request = VehicleRequest(
                task_id=data.get('task_id'),
                no_of_vehicles=data.get('no_of_vehicles'),
                purpose_of_visit=data.get('purpose_of_visit'),
                vehicle_types=",".join(data.get('vehicle_types', [])),
                special_requirements=data.get('special_requirements'),
            )
            vehicle_request.save()
            return JsonResponse({'success': True, 'message': 'Form submitted successfully!'})
        except json.JSONDecodeError as e:
            return JsonResponse({'success': False, 'message': f'Invalid JSON: {e}'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error: {e}'}, status=500)
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def submit_accommodation_form(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print('Received Data:', data)
            # Process form data
            acc=AccommodationRequest(
            task_id = data.get('task_id'),
            no_of_participants = data.get('no_of_participants'),
            no_of_guests = data.get('no_of_guests', 0),
            accommodation_type = data.get('accommodation_type'),
            special_requirements = data.get('special_requirements'),
            arrival_date = data.get('arrival_date'),
            departure_date = data.get('departure_date'),)
            acc.save()

            # Save to database or perform further processing here

            return JsonResponse({'success': True, 'message': 'Form submitted successfully!'})
        except json.JSONDecodeError as e:
            return JsonResponse({'success': False, 'message': f'Invalid JSON: {str(e)}'})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})
#adminend




def admin_event_list(request):
    # Fetch all events along with related foreign key data
    events = Event.objects.all()
    venue_requests = VenueRequest.objects.all()
    photography_requests = PhotographyRequest.objects.all()
    accessories_requests = AccessoriesRequest.objects.all()
    vehicle_requests = VehicleRequest.objects.all()
    accommodation_requests = AccommodationRequest.objects.all()
    venue_requests = {v.task_id: v for v in VenueRequest.objects.all()}
    photography_requests={v.task_id: v for v in PhotographyRequest.objects.all()}
    accessories_requests={v.task_id: v for v in AccessoriesRequest.objects.all()}
    vehicle_requests={v.task_id: v for v in VehicleRequest.objects.all()}
    accommodation_requests={v.task_id: v for v in AccommodationRequest.objects.all()}
    # Pass data to template
    context = {
        'events': events,
        'venue_requests': venue_requests,
        'photography_requests': photography_requests,
        'accessories_requests': accessories_requests,
        'vehicle_requests': vehicle_requests,
        'accommodation_requests': accommodation_requests,
    }
    return render(request, 'admin_event_list.html', {
        'events': events,
        'venue_requests': venue_requests,
        'photography_requests':photography_requests,
        'accessories_requests': accessories_requests,
        'vehicle_requests': vehicle_requests,
        'accommodation_requests': accommodation_requests,
    })

def approve_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.approval_status = 'approved'
    event.admin_comments = request.POST.get('admin_comments', '')
    event.save()
    return redirect('admin_event_list')

def reject_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.approval_status = 'rejected'
    event.admin_comments = request.POST.get('admin_comments', '')
    event.save()
    return redirect('admin_event_list')

def RoleSelection(request):
    return render(request, 'RoleSelection.html')
def register(request):
    return render(request, 'Register.html')
def userlogin(request):
    return render(request, 'userlogin.html')
def adminlogin(request):
    return render(request, 'adminlogin.html')
def user_profile(request):
    return render(request, 'user.html')

def venue(request):
    return render(request, 'venue.html')

def photography(request):
    return render(request, 'photography.html')

def accessories(request):
    return render(request, 'accessories.html')

def vehicle(request):
    return render(request, 'vehicle.html')

def accommodation(request):
    return render(request, 'accommodation.html')

def forms(request):
    return render(request, 'forms.html')

def home_view(request):
    return render(request, 'home.html')

def admin_view(request):
    return render(request, 'admin.html')

def user_view(request):
    return render(request, 'user.html')


