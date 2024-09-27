from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Appointment
from .forms import PatientForm, AppointmentForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        patient_form = PatientForm(request.POST)
        if form.is_valid() and patient_form.is_valid():
            user = form.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        patient_form = PatientForm()
    return render(request, 'patients/register.html', {'form': form, 'patient_form': patient_form})

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
        form = AppointmentForm()
    return render(request, 'patients/schedule.html', {'form': form})