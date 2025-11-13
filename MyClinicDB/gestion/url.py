from django.urls import path
from .views import PacienteListView, PacienteCreateView, DoctorListView,DoctorCreateView
from .views import pacienteDetailView, pacienteUpdateView, pacienteDeleteView
from .views import doctorDetailView, doctorUpdateView, doctorDeleteView
from .views import CitaListView, CitaCreateView, citaDeleteView, citaUpdateView, citaDetailView


app_name = 'gestion'


urlpatterns = [
    path('pacientes/', PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/crear/', PacienteCreateView.as_view(), name='paciente_create'),
    path('doctores/', DoctorListView.as_view(), name='doctor_list'),
    path('doctores/crear/', DoctorCreateView.as_view(), name='doctor_create'),
    path('pacientes/<int:pk>/', pacienteDetailView.as_view(), name='paciente_detail'),
    path('pacientes/<int:pk>/editar/', pacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/<int:pk>/eliminar/', pacienteDeleteView.as_view(), name='paciente_delete'),
    path('doctores/<int:pk>/', doctorDetailView.as_view(), name='doctor_detail'),
    path('doctores/<int:pk>/editar/', doctorUpdateView.as_view(), name='doctor_update'),
    path('doctores/<int:pk>/eliminar/', doctorDeleteView.as_view(), name='doctor_delete'),
    path('citas/', CitaListView.as_view(), name='cita_list'),
    path('citas/crear/', CitaCreateView.as_view(), name='cita_create'),
    path('citas/<int:pk>/', citaDetailView.as_view(), name='cita_detail'),
    path('citas/<int:pk>/editar/', citaUpdateView.as_view(), name='cita_update'),
    path('citas/<int:pk>/eliminar/', citaDeleteView.as_view(), name='cita_delete'),
]