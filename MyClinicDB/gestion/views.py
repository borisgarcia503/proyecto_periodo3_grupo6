from django.shortcuts import render
from .models import Paciente, Doctor, Cita
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PacienteForm, DoctorForm, CitaForm
# Create your views here.

class PacienteListView(ListView):
    model = Paciente
    template_name = 'pacientes/paciente_list.html'
    context_object_name = 'pacientes'

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('gestion:paciente_list')

class pacienteDetailView(DetailView):
    model = Paciente
    template_name = 'pacientes/paciente_detail.html'
    context_object_name = 'paciente'

class pacienteUpdateView(UpdateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'email', 'telefono']
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('gestion:paciente_list')

class pacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'pacientes/paciente_confirm_delete.html'
    success_url = reverse_lazy('gestion:paciente_list')

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctores/doctor_list.html'
    context_object_name = 'doctores'

class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctores/doctor_form.html'
    success_url = reverse_lazy('gestion:doctor_list')

class doctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctores/doctor_detail.html'
    context_object_name = 'doctor'

class doctorUpdateView(UpdateView):
    model = Doctor
    fields = ['nombre', 'apellido', 'especialidad', 'email', 'telefono']
    template_name = 'doctores/doctor_form.html'
    success_url = reverse_lazy('gestion:doctor_list')

class doctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctores/doctor_confirm_delete.html'
    success_url = reverse_lazy('gestion:doctor_list')

class CitaListView(ListView):
    model = Cita
    template_name = 'citas/cita_list.html'
    context_object_name = 'citas'

class CitaCreateView(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'citas/cita_form.html'
    success_url = reverse_lazy('gestion:cita_list')

class citaDetailView(DetailView):
    model = Cita
    template_name = 'citas/cita_detail.html'
    context_object_name = 'cita'

class citaUpdateView(UpdateView):
    model = Cita
    fields = ['paciente', 'doctor', 'fecha_hora', 'motivo']
    template_name = 'citas/cita_form.html'
    success_url = reverse_lazy('gestion:cita_list')

class citaDeleteView(DeleteView):
    model = Cita
    template_name = 'citas/cita_confirm_delete.html'
    success_url = reverse_lazy('gestion:cita_list')




