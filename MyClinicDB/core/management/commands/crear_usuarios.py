from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission

class Command(BaseCommand):
    help = "Crear usuarios y grupos de prueba"

    def handle(self, *args, **kwargs):

        # Crear grupos
        roles = ['Paciente', 'Doctor', 'Administrador']
        grupos = {}
        for role in roles:
            grupo, _ = Group.objects.get_or_create(name=role)
            grupos[role] = grupo

        # El administrador tiene todos los permisos
        grupos['Administrador'].permissions.set(Permission.objects.all())

        # Crear usuarios
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_user(username='admin', password='adminpass')
            admin_user.is_staff = True
            admin_user.is_superuser = True
            admin_user.groups.add(grupos['Administrador'])
            admin_user.save()
            self.stdout.write(self.style.SUCCESS("Usuario admin creado"))

        if not User.objects.filter(username='doctor1').exists():
            doctor_user = User.objects.create_user(username='doctor1', password='doctorpass')
            doctor_user.groups.add(grupos['Doctor'])
            doctor_user.save()
            self.stdout.write(self.style.SUCCESS("Usuario doctor1 creado"))

        if not User.objects.filter(username='paciente1').exists():
            paciente_user = User.objects.create_user(username='paciente1', password='pacientepass')
            paciente_user.groups.add(grupos['Paciente'])
            paciente_user.save()
            self.stdout.write(self.style.SUCCESS("Usuario paciente1 creado"))
