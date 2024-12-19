from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.decorators import login_required
import logging
from .models import * 
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
logger = logging.getLogger(__name__) 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core import serializers
import json
from datetime import date
from PIL import Image
@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Ensure the user has a profile
                if not hasattr(user, 'profile'):
                    Profile.objects.create(user=user)
                auth_login(request, user)
                return redirect('home')  # Replace 'home' with your desired redirect URL
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
# @csrf_exempt
# def forgot_password(request):
#     if request.method == 'POST':
#         old_password = request.POST.get('old_password')
#         new_password = request.POST.get('new_password')
#         confirm_password = request.POST.get('confirm_password')

#         # Validate old password
#         if not request.user.check_password(old_password):
#             messages.error(request, 'Your old password is incorrect.')
#             return render(request, 'admin/Forgotpassword.html')

#         # Validate new password and confirmation
#         if new_password != confirm_password:
#             messages.error(request, 'New password and confirm password do not match.')
#             return render(request, 'admin/Forgotpassword.html')

#         if len(new_password) < 8:
#             messages.error(request, 'New password must be at least 8 characters long.')
#             return render(request, 'admin/Forgotpassword.html')

#         # Update password
#         request.user.set_password(new_password)
#         request.user.save()

#         # Ensure the user remains logged in after the password change
#         update_session_auth_hash(request, request.user)

#         messages.success(request, 'Your password has been successfully updated.')
#         return redirect('home')  # Replace 'home' with your desired redirect page after password change

#     return render(request, 'admin/Forgotpassword.html')
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'Forgotpassword.html'
    success_url = reverse_lazy('password_change_done')
    login_url = '/login/'  # Specify your custom login page

    def handle_no_permission(self):
        # Redirect to the login page or show a custom error
        return redirect(self.login_url)
def logout(request):
    auth_logout(request)
    return redirect('login')

# @csrf_exempt
# def adminhome(request):
#     return render(request, 'Adminhome.html')

def dashboard(request):
    return render(request, 'Dashboard/dashboard.html')  

def home(request):
    return render(request, 'Home/Home.html')

@csrf_exempt
def banner_list(request):
    banners = HomePageBanner.objects.all().order_by('id')
    if request.headers.get('Content-Type') == 'application/json' or request.headers.get('Accept') == 'application/json':
        banner_data = serializers.serialize('json', banners)
        return JsonResponse(banner_data, safe=False)
    return render(request, 'Home/banner_list.html', {'banners': banners})


def banner_add(request):
    if request.method == 'POST':
        form = HomePageBannerForm(request.POST, request.FILES)
        if form.is_valid():
            banner = form.save(commit=False)

            image_file = request.FILES.get('home_page_banner_image', None)

            # Handle image upload
            if image_file:
                banner.file_size = image_file.size
                try:
                    with Image.open(image_file) as img:
                        banner.width = img.width
                        banner.height = img.height
                        banner.format = img.format if img.format else 'Unknown'
                except Exception as e:
                    print(f"Error processing image: {e}")
                    banner.width = 0
                    banner.height = 0
                    banner.format = 'Unknown'

            # Save the banner instance
            banner.save()

            return redirect('banner_list')
    else:
        form = HomePageBannerForm()

    return render(request, 'Home/banner_form.html', {'form': form})


def banner_edit(request, pk):
    banner = get_object_or_404(HomePageBanner, pk=pk)
    if request.method == "POST":
        form = HomePageBannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            return redirect('banner_list')
    else:
        form = HomePageBannerForm(instance=banner)
    return render(request, 'Home/banner_form.html', {'form': form})


def banner_delete(request, pk):
    banner = get_object_or_404(HomePageBanner, pk=pk)
    banner.delete()
    return redirect('banner_list')

@csrf_exempt
def subscribe_list(request):
    subscribes = HomePageSubscribeForm.objects.all().order_by('id')
    if request.headers.get('Content-Type') == 'application/json' or request.headers.get('Accept') == 'application/json':
        subscribe_data = serializers.serialize('json', subscribes)
        return JsonResponse(subscribe_data, safe=False)
    return render(request, 'Home/subscribe_list.html', {'subscribes': subscribes})

def subscribe_add(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST, request.FILES)
        if form.is_valid():
            subscribe = form.save(commit=False)
            subscribe.save()
            return redirect('subscribe_list')
    else:
        form =()
    return render(request, 'Home/subscribe_form.html', {'form': form})

def subscribe_edit(request, pk):
    subscribe = get_object_or_404(HomePageSubscribeForm, pk=pk)
    if request.method == "POST":
        form = SubscribeForm(request.POST, request.FILES, instance=subscribe)
        if form.is_valid():
            form.save()
            return redirect('subscribe_list')
    else:
        form = SubscribeForm(instance=subscribe)
    return render(request, 'Home/subscribe_form.html', {'form': form})

def subscribe_delete(request, pk):
    subscribe = get_object_or_404(HomePageSubscribeForm, pk=pk)
    subscribe.delete()
    return redirect('subscribe_list')

@csrf_exempt
def tickets_price_list(request):
    tickets = HomePageTicketsPrice.objects.all().order_by('id')
    if request.headers.get('Content-Type') == 'application/json' or request.headers.get('Accept') == 'application/json':
        tickets_data = serializers.serialize('json', tickets)
        return JsonResponse(tickets_data, safe=False)
    return render(request, 'Home/tickets_price_list.html', {'tickets': tickets})

def tickets_price_add(request):
    if request.method == 'POST':
        form = HomePageTicketsPrice(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.save()
            return redirect('tickets_price_list')
    else:
        form = TicketsPriceForm()
    return render(request, 'Home/tickets_price_form.html', {'form': form})

def tickets_price_edit(request, pk):
    ticket = get_object_or_404(HomePageTicketsPrice, pk=pk)
    if request.method == "POST":
        form = TicketsPriceForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('tickets_price_list')
    else:
        form = TicketsPriceForm(instance=ticket)
    return render(request, 'Home/tickets_price_form.html', {'form': form})

def tickets_price_delete(request, pk):
    ticket = get_object_or_404(HomePageTicketsPrice, pk=pk)
    ticket.delete()
    return redirect('tickets_price_list')


def mettings(request):
    return render(request, 'Home/Meetings.html')

def blogs(request):
    return render(request, 'Home/Blogs.html')

def meetings(request):
    return render(request, 'Home/Meetings.html')

def contact(request):
    return render(request, 'Home/Contact.html')