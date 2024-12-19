from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy, path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('password-change-done/', PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'
    ), name='password_change_done'),
    path('logout/', logout, name='logout'),
    # path('adminhome/', adminhome, name='adminhome'),
    path('dashboard/', dashboard, name='dashboard'),
    path('home/', home, name='home'),
    path('home/blogs/', blogs, name='blogs'),
    path('home/meetings/', meetings, name='meetings'),
    path('home/contact/', contact, name='contact'),
    
    path('home/banners/', banner_list, name='banner_list'),
    path('home/banners/add/', banner_add, name='banner_add'),
    path('home/banners/edit/<int:pk>/', banner_edit, name='banner_edit'),
    path('home/banners/delete/<int:pk>/', banner_delete, name='banner_delete'),
    
    path('home/subscribe/', subscribe_list, name='subscribe_list'),
    path('home/subscribe/add/', subscribe_add, name='subscribe_add'),
    path('home/subscribe/edit/<int:pk>/', subscribe_edit, name='subscribe_edit'),
    path('home/subscribe/delete/<int:pk>/', subscribe_delete, name='subscribe_delete'),
    
    path('home/tickets_price/', tickets_price_list, name='tickets_price_list'),
    path('home/tickets_price/add/', tickets_price_add, name='tickets_price_add'),
    path('home/tickets_price/edit/<int:pk>/', tickets_price_edit, name='tickets_price_edit'),
    path('home/tickets_price/delete/<int:pk>/', tickets_price_delete, name='tickets_price_delete'),
]
