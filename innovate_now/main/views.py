from django.shortcuts import render, redirect, get_object_or_404
from .models import NavbarItem, About, Service
from .forms import NavbarItemForm, AboutForm, ServiceForm

# Vistas para las páginas principales
def home(request):
    navbar_items = NavbarItem.objects.all()
    services = Service.objects.all()
    return render(request, 'main/home.html', {'navbar_items': navbar_items, 'services': services})
def about(request):
    navbar_items = NavbarItem.objects.all()
    about_info = About.objects.all()
    return render(request, 'main/about.html', {'navbar_items': navbar_items, 'about_info': about_info})

def services(request):
    navbar_items = NavbarItem.objects.all()
    services = Service.objects.all()
    return render(request, 'main/services.html', {'navbar_items': navbar_items, 'services': services})


def service_list(request):
    services = Service.objects.all()
    return render(request, 'main/service_list.html', {'services': services})

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'main/service_form.html', {'form': form})

def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'main/service_form.html', {'form': form})

def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'main/service_confirm_delete.html', {'service': service})
