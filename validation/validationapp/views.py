# # validation/views.py
# from django.shortcuts import redirect, render
# from .forms import RegisterForm,VehicleForm



# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#     else:
#         form = RegisterForm()

#     return render(request, 'registration/register.html', {'form': form})

# def register_vehicle_view(request):
#     if request.method == 'POST':
#         form = VehicleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             #return redirect('vehicle')  # Redirect to a success page or another view
#     else:
#         form = VehicleForm()

#     return render(request, 'registration/register_vehicle.html', {'form': form})


# validation/views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm, VehicleForm
from django.forms import formset_factory

def register_view(request):
    VehicleFormSet = formset_factory(VehicleForm, extra=1, can_delete=True)

    if request.method == 'POST':
        participant_form = RegisterForm(request.POST)
        vehicle_formset = VehicleFormSet(request.POST, prefix='vehicles')

        if participant_form.is_valid() and vehicle_formset.is_valid():
            participant = participant_form.save()
            for form in vehicle_formset:
                if not form.cleaned_data.get('DELETE', False):
                    vehicle = form.save(commit=False)
                    vehicle.participant = participant
                    vehicle.save()

            # Redirect to a success page
            return redirect('form_success')
    else:
        participant_form = RegisterForm()
        vehicle_formset = VehicleFormSet(prefix='vehicles')

    return render(request, 'registration/register.html', {'participant_form': participant_form, 'vehicle_formset': vehicle_formset})

def form_success_view(request):
    return render(request, 'form_success.html')

def register_vehicle_view(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            # Save the form data to the database or perform any other necessary actions
            form.save()
            # Redirect to a success page or another view
            return redirect('form_success')
    else:
        form = VehicleForm()

    return render(request, 'registration/register_vehicle.html', {'form': form})


def form_success_view(request):
    return render(request, 'form_success.html')
