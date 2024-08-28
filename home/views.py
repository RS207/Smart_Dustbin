from django.shortcuts import render, HttpResponse, Http404,redirect
import os
import random
from django.conf import settings
from home.models import Contact
from django.contrib import messages
from django.conf import settings
from django.templatetags.static import static
from django.utils.crypto import get_random_string


def random_image_view(request, folder_name):
    """
    This view returns a random image from the specified folder inside 'static/images/'.
    """
    # Construct the folder path
    img_folder = os.path.join(settings.STATICFILES_DIRS[0], 'images', folder_name)
    
    try:
        # List all images in the folder
        images = os.listdir(img_folder)
        images = [img for img in images if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        if not images:
            raise FileNotFoundError("No images found in this folder.")
        
        # Generate a unique cache-busting parameter
        unique_id = get_random_string(12)  # Generate a random string for uniqueness

        # Choose a random image
        random_image = random.choice(images)

        # Construct the image URL with a unique cache-busting parameter
        image_url = static(f'images/{folder_name}/{random_image}')
        full_image_url = f'{image_url}?unique_id={unique_id}'

        # Return the image file
        with open(os.path.join(img_folder, random_image), 'rb') as img_file:
            return HttpResponse(img_file.read(), content_type='image/jpeg')
    
    except FileNotFoundError:
        raise Http404("No images found in this folder.")


# Create your views here.
def index(request):
    return render(request, 'index.html')

def management(request):
    return render(request, 'management.html')

def services(request):
    return render(request, 'services.html')

def collaborations(request):
    return render(request, 'collaborations.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        country_code = request.POST.get('country_code')
        contact_number = request.POST.get('contact')
        desc = request.POST.get('message')
        entry = Contact(name=name, email=email,country_code=country_code,contact_number=contact_number,desc = desc)
        entry.save()
        messages.success(request, "Your message has been sent.")
        return redirect('contact')

    return render(request, 'contact.html')

def team(request):
    return render(request, 'team.html')