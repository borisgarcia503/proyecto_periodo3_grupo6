from django import forms
from .models import Paciente, Doctor, Cita


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre paciente'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido paciente'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email paciente'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono paciente'}),
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'apellido', 'especialidad', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre doctor'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido doctor'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especialidad doctor'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email doctor'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono doctor'}),

        }

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'doctor', 'fecha_hora', 'motivo']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione un paciente'}),
            'doctor': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione un doctor'}),
            'fecha_hora': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Motivo de la cita'}),
        }