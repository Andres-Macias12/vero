# comercios/views.py
from django.db.models import Q 
from .models import Comercio, Novedad
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ComercioForm, NovedadForm, UserRegistrationForm  
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User


def lista_comercios(request):
    query = request.GET.get('q')  # Consulta de búsqueda
    categoria = request.GET.get('categoria')  # Obtener la categoría seleccionada
    comercios = Comercio.objects.all()

    # Filtrar por nombre si se ingresa una búsqueda
    if query:
        comercios = comercios.filter(Q(nombre__icontains=query) | Q(categoria__icontains=query))
    
    # Filtrar por categoría si se selecciona una
    if categoria and categoria != 'todas':
        comercios = comercios.filter(categoria=categoria)
    
    # Obtener los comercios destacados como novedades
    comercios_novedad = Comercio.objects.filter(novedad=True)
    
    # Obtener todas las categorías disponibles para el menú desplegable
    categorias_disponibles = Comercio.objects.values_list('categoria', flat=True).distinct()
    
    return render(request, 'comercios/lista_comercios.html', {
        'comercios': comercios,
        'comercios_novedad': comercios_novedad,
        'categorias_disponibles': categorias_disponibles,
        'query': query,
        'categoria': categoria
    })

def pagina_principal(request):
    novedades = Novedad.objects.order_by('-fecha_publicacion')[:5]  # Mostrar las 5 últimas novedades
    return render(request, 'comercios/pagina_principal.html', {'novedades': novedades})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            return redirect('login')  # Redirige a la página de inicio de sesión o actualiza al nombre correcto
    else:
        form = UserRegistrationForm()
    return render(request, 'comercios/register_user.html', {'form': form})

# Vistas para Comercio
class ComercioListView(ListView):
    model = Comercio
    template_name = 'comercios/comercio_list.html'
    context_object_name = 'comercios'

class ComercioDetailView(DetailView):
    model = Comercio
    template_name = 'comercios/comercio_detail.html'

class ComercioCreateView(CreateView):
    model = Comercio
    form_class = ComercioForm
    template_name = 'comercios/comercio_form.html'
    success_url = reverse_lazy('comercio-list')

class ComercioUpdateView(UpdateView):
    model = Comercio
    form_class = ComercioForm
    template_name = 'comercios/comercio_form.html'
    success_url = reverse_lazy('comercio-list')

class ComercioDeleteView(DeleteView):
    model = Comercio
    template_name = 'comercios/comercio_confirm_delete.html'
    success_url = reverse_lazy('comercio-list')

# Vistas para Novedad
class NovedadListView(ListView):
    model = Novedad
    template_name = 'comercios/novedad_list.html'
    context_object_name = 'novedades'

class NovedadDetailView(DetailView):
    model = Novedad
    template_name = 'comercios/novedad_detail.html'

class NovedadCreateView(CreateView):
    model = Novedad
    form_class = NovedadForm
    template_name = 'comercios/novedad_form.html'
    success_url = reverse_lazy('novedad-list')

class NovedadUpdateView(UpdateView):
    model = Novedad
    form_class = NovedadForm
    template_name = 'comercios/novedad_form.html'
    success_url = reverse_lazy('novedad-list')

class NovedadDeleteView(DeleteView):
    model = Novedad
    template_name = 'comercios/novedad_confirm_delete.html'
    success_url = reverse_lazy('novedad-list')

