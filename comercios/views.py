# comercios/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Comercio, Novedad, Message
from .forms import ComercioForm, NovedadForm, UserRegistrationForm

def chat_view(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(user=request.user, content=content)
        return redirect('chat')

    messages = Message.objects.all().order_by('-timestamp')[:50]
    return render(request, 'comercios/chat.html', {'messages': messages})

def get_messages(request):
    messages = Message.objects.all().order_by('-timestamp')[:50]
    return JsonResponse({'messages': list(messages.values())})

def lista_comercios(request):
    query = request.GET.get('q')
    categoria = request.GET.get('categoria')
    comercios = Comercio.objects.all()

    if query:
        comercios = comercios.filter(Q(nombre__icontains=query) | Q(categoria__icontains=query))
    
    if categoria and categoria != 'todas':
        comercios = comercios.filter(categoria=categoria)
    
    comercios_novedad = Comercio.objects.filter(novedad=True)
    categorias_disponibles = Comercio.objects.values_list('categoria', flat=True).distinct()
    
    return render(request, 'comercios/lista_comercios.html', {
        'comercios': comercios,
        'comercios_novedad': comercios_novedad,
        'categorias_disponibles': categorias_disponibles,
        'query': query,
        'categoria': categoria
    })

def pagina_principal(request):
    novedades = Novedad.objects.order_by('-fecha_publicacion')[:5]
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
            return redirect('login')
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
