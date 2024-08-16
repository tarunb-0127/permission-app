# restricted/views.py
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from .models import RestrictedPage

class CustomLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'login.html'

def check_permission(request):
    user = request.user
    can_access = user.has_perm('restricted.view_restrictedpage')
    return render(request, 'check_permission.html', {'can_access': can_access})

def restricted_page(request):
    page_content = RestrictedPage.objects.first()  # Assuming only one restricted page exists
    return render(request, 'restricted_page.html', {'page_content': page_content})
