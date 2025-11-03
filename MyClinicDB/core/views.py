from django.shortcuts import render
#importar vistas de autentificacion
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = '/core/login/'  # Redirect to login page after logout

def principal_view(request):
    return render(request, 'core/principal.html')