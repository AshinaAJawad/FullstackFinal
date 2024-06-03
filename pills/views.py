from django.shortcuts import get_object_or_404, render, redirect
from .models import Medicine
from django.contrib.auth.decorators import login_required
from .forms import MedicineForm
@login_required
def medicine_list(request):
    if request.user.is_authenticated:
        medicine = Medicine.objects.filter(user=request.user)
    else:
        medicine = Medicine.objects.none()
    return render(request, 'pills/medicine_list.html', {'medicine': medicine})
@login_required
def add_medicine(request):
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.days = ",".join(form.cleaned_data['days'])
            times = []
            dose = int(form.cleaned_data['dose'])
            for i in range(dose):
                time_field = f'time_{i}'
                if time_field in request.POST:
                    times.append(request.POST[time_field])
            medicine.times = times
            medicine.user = request.user
            medicine.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'pills/add_medicine.html', {'form': form})
@login_required
def update_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == "POST":
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.days = ",".join(form.cleaned_data['days'])
            medicine.save()
            return redirect('medicine_list')  
    else:
        initial_data = medicine.__dict__
        initial_data['days'] = medicine.days.split(',')
        form = MedicineForm(initial=initial_data, instance=medicine)
    return render(request, 'pills/update_medicine.html', {'form': form})
@login_required
def delete_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == "POST":
        medicine.delete()
        return redirect('medicine_list')
    return render(request, 'pills/delete_medicine.html', {'medicine': medicine})

@login_required
def about(request):
    return render(request, 'pills/about.html')
