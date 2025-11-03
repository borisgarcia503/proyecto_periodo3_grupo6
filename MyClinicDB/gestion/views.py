from django.shortcuts import render
from .models import Paciente, Doctor, Cita
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PacienteForm, DoctorForm, CitaForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@login_required
def lista_principal(request):
    return render(request, 'gestion/index.html')

@method_decorator(login_required, name='dispatch')
class PacienteListView(ListView):
    model = Paciente
    template_name = 'pacientes/paciente_list.html'
    context_object_name = 'pacientes'

@method_decorator(login_required, name='dispatch')
class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('gestion:paciente_list')

@method_decorator(login_required, name='dispatch')
class pacienteDetailView(DetailView):
    model = Paciente
    template_name = 'pacientes/paciente_detail.html'
    context_object_name = 'paciente'

@method_decorator(login_required, name='dispatch')
class pacienteUpdateView(UpdateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'email', 'telefono']
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('gestion:paciente_list')

@method_decorator(login_required, name='dispatch')
class pacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'pacientes/paciente_confirm_delete.html'
    success_url = reverse_lazy('gestion:paciente_list')

@method_decorator(login_required, name='dispatch')
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctores/doctor_list.html'
    context_object_name = 'doctores'

@method_decorator(login_required, name='dispatch')
class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctores/doctor_form.html'
    success_url = reverse_lazy('gestion:doctor_list')

@method_decorator(login_required, name='dispatch')
class doctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctores/doctor_detail.html'
    context_object_name = 'doctor'

@method_decorator(login_required, name='dispatch')
class doctorUpdateView(UpdateView):
    model = Doctor
    fields = ['nombre', 'apellido', 'especialidad', 'email', 'telefono']
    template_name = 'doctores/doctor_form.html'
    success_url = reverse_lazy('gestion:doctor_list')

@method_decorator(login_required, name='dispatch')
class doctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctores/doctor_confirm_delete.html'
    success_url = reverse_lazy('gestion:doctor_list')

@method_decorator(login_required, name='dispatch')
class CitaListView(ListView):
    model = Cita
    template_name = 'citas/cita_list.html'
    context_object_name = 'citas'

@method_decorator(login_required, name='dispatch')
class CitaCreateView(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'citas/cita_form.html'
    success_url = reverse_lazy('gestion:cita_list')

@method_decorator(login_required, name='dispatch')
class citaDetailView(DetailView):
    model = Cita
    template_name = 'citas/cita_detail.html'
    context_object_name = 'cita'

@method_decorator(login_required, name='dispatch')
class citaUpdateView(UpdateView):
    model = Cita
    fields = ['paciente', 'doctor', 'fecha_hora', 'motivo']
    template_name = 'citas/cita_form.html'
    success_url = reverse_lazy('gestion:cita_list')

@method_decorator(login_required, name='dispatch')
class citaDeleteView(DeleteView):
    model = Cita
    template_name = 'citas/cita_confirm_delete.html'
    success_url = reverse_lazy('gestion:cita_list')




