from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Provider, Schedule
from .forms import ScheduleForm

@login_required
def profile(request):
    provider = Provider.objects.get(user=request.user)
    return render(request, 'providers/profile.html', {'provider': provider})

@login_required
def manage_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.provider = Provider.objects.get(user=request.user)
            schedule.save()
            return redirect('profile')
    else:
        form = ScheduleForm()
    return render(request, 'providers/appointments.html', {'form': form})