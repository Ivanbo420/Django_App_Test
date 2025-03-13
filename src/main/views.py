from importlib import reload
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Listing, LikedListing
from .forms import ListingForm
from users.forms import LocationForm
from django.contrib import messages
from .filters import ListingFilter
import uuid
from django.shortcuts import get_object_or_404
from django.contrib.humanize.templatetags.humanize import intcomma
import phonenumbers

def landing_view(request):
    return render(request, "views/main.html", {"name":"Automax"})

@login_required
def home_view(request):
    listings= Listing.objects.all()
    listing_filter= ListingFilter(request.GET, queryset=listings)
    user_like_listing= LikedListing.objects.filter(profile=request.user.profile).values_list('listing')
    liked_listings_id= [l[0] for l in user_like_listing]
    print(liked_listings_id)
    context= {'listing_filter':listing_filter,'liked_listings_id':liked_listings_id,}
    return render(request, "views/home.html", context)

@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form= ListingForm(request.POST, request.FILES)
            location_form= LocationForm(request.POST)
            if listing_form.is_valid() and location_form.is_valid():
                listing= listing_form.save(commit=False)
                listing_location= location_form.save()
                listing.seller= request.user.profile
                listing.location= listing_location
                listing.save()
                messages.info(request, f' {listing.model} Listed successfully.')
                return redirect('home')
            else:
                raise Exception()
        except Exception as e:
            print(e)
            messages.error(request, 'An error occured while listing...')
    elif request.method == 'GET':
        listing_form= ListingForm()
        location_form= LocationForm()
    return render(request, "views/list.html", {'listing_form':listing_form, 'location_form':location_form})

#Codigo original que no me funciona, no se por que
'''@login_required
def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        return render(request, 'views/listing.html', {'listing': listing, })
    except Exception as e:
        messages.error(request, f'Invalid UID {id} was provided for listing.')
        return redirect('home') '''

#Solucion alternativa
@login_required
def listing_view(request, id):
    try:
        if not isinstance(id, uuid.UUID):
            id = uuid.UUID(id)

        listing = Listing.objects.filter(id=id).first()

        if listing is None:
            return HttpResponse(f"Listing with ID {id} not found!", status=404)
        
        #Agregado propio para formatear unidades de mil 
        formatted_mileage = intcomma(listing.mileage).replace(",", ".")

        #Agregado propio para formatear numero de telefono
        formatted_phone_number = listing.seller.phone_number  # Default raw number
        try:
            parsed_number = phonenumbers.parse(listing.seller.phone_number, None)
            if phonenumbers.is_valid_number(parsed_number):
                formatted_phone_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        except phonenumbers.NumberParseException:
            pass  # Keep raw number if parsing fails
        
        return render(request, 'views/listing.html', {'listing': listing, 'formatted_mileage': formatted_mileage, 'formatted_phone_number':formatted_phone_number, })
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)
    
@login_required
def edit_view(request, id):
    try:
        listing= Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        if request.method=='POST':
            listing_form= ListingForm(request.POST, request.FILES , instance=listing)
            location_form= LocationForm(request.POST, instance=listing.location)
            if listing_form.is_valid and location_form.is_valid:
                listing_form.save()
                location_form.save()
                messages.info(request, f'Listing {id} updated successfully.')
                return redirect('home')
            else:
                messages.error(request, f'An error occured while trying to edit the listing.')
                return reload()
        else:
            listing_form= ListingForm(instance=listing)
            location_form= LocationForm(instance=listing.location)
        context= {'location_form':location_form, 'listing_form':listing_form, }
        return render(request, 'views/edit.html', context)
    except Exception as e:
        messages.error(request, f'An error occured while trying to edit the listing.')
        return redirect('home')

@login_required
def like_listing_view(request, id):
    listing= get_object_or_404(Listing, id=id)
    liked_listing, created= LikedListing.objects.get_or_create(profile= request.user.profile, listing=listing)
    if not created:
        liked_listing.delete()
    else:
        liked_listing.save()
    return JsonResponse({'is_liked':created})