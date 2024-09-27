from django.shortcuts import render, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointments/detail.html', {'appointment': appointment})