from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    return render(request, 'index.html', {})
 # Servicios
def cortes(request):
    return render(request, 'cortes.html', {})

def barba(request):
    return render(request, 'barba.html', {})

def contornos(request):
    return render(request, 'contornos.html', {})

def ceja(request):
    return render(request, 'ceja.html', {})

def mascarilla(request):
    return render(request, 'mascarilla.html', {})
# Productos
def pomada(request):
    return render(request, 'pomada.html', {})

def after(request):
    return render(request, 'after.html', {})

def shampoo(request):
    return render(request, 'shampoo.html', {})

def aceites(request):
    return render(request, 'aceites.html', {})

def talco(request):
    return render(request, 'talco.html', {})
# Contacto
def citas(request):
    return render(request, 'citas.html', {})

def redes(request):
    return render(request, 'redes.html', {})

def mensaje(request):
    return render(request, 'mensaje.html', {})

def ubicacion(request):
    return render(request, 'ubicacion.html', {})
# Forms get started sing in
def formStart(request):
    return render(request, 'formStart.html', {})

def formSing(request):
    return render(request, 'formSing.html', {})

# Vistas ade los fokrmularios.

def citaSuccess(request):
    name = request.POST['name']
    return render(request, 'citaSuccess.html', {"name": name})

def inicioSuccess(request):
    if request.method != 'POST':
        return HttpResponse("El metodo GET no est soportado por esta ruta")
    info = request.POST['info']
    return render(request, 'inicioSuccess.html', {"info": info})
    
    