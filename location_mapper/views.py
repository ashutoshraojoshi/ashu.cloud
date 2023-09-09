# location_mapper/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Location
from .forms import LocationForm
from geopy.geocoders import Nominatim
from urllib.parse import urlparse, parse_qs
from .utils import extract_coordinates_from_google_maps_url
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def location_list(request):
    # Retrieve locations associated with the authenticated user
    locations = Location.objects.filter(user=request.user)
    return render(request, 'location_mapper/location_list.html', {'locations': locations})

def location_detail(request, custom_name):
    location = get_object_or_404(Location, custom_name=custom_name)
    latitude, longitude, garbage = extract_coordinates_from_google_maps_url(location.google_maps_url)
    ll = {'latitude':latitude,'longitude':longitude}
    return render(request, 'location_mapper/location_detail.html', {'location': location, 'll':ll})

@login_required
def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            google_maps_url = form.cleaned_data['google_maps_url']
            print(google_maps_url)
            # Extract latitude and longitude from the Google Maps URL
            latitude, longitude, garbage = extract_coordinates_from_google_maps_url(google_maps_url)
            
            print("Google Maps URL:", google_maps_url)
            print("Extracted Latitude:", latitude)
            print("Extracted Longitude:", longitude)
            
            # Check if a location with the same custom_name already exists
            existing_location = Location.objects.filter(custom_name=location.custom_name).first()

            if existing_location:
                # Display a prompt that the custom name already exists
                prompt_message = f"A location with the custom name '{location.custom_name}' already exists."
                return render(request, 'location_mapper/add_location.html', {'form': form, 'prompt_message': prompt_message})

            if latitude and longitude:
                location.latitude = latitude
                location.longitude = longitude
                user = User.objects.get(username=request.user)  # Replace with the actual user
                location = Location(custom_name=location.custom_name, google_maps_url=location.google_maps_url, user=user)
                location.save()
                return redirect('location_list')
            else:
                # Handle invalid Google Maps URL here
                error_message = "Invalid Google Maps URL. Please check the format."
                print("Error:", error_message)
                return render(request, 'location_mapper/add_location.html', {'form': form, 'error_message': error_message})
        else:
            print("Form is not valid. Form errors:", form.errors)
    else:
        form = LocationForm()
    return render(request, 'location_mapper/add_location.html', {'form': form})
