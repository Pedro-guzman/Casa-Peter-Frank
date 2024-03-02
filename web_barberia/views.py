from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    return render(request, 'index.html', {})
 # Servicios
def cortes(request):
    return render(request, 'servicios/cortes.html', {})

def barba(request):
    return render(request, 'servicios/barba.html', {})

def contornos(request):
    return render(request, 'servicios/contornos.html', {})

def ceja(request):
    return render(request, 'servicios/ceja.html', {})

def mascarilla(request):
    return render(request, 'servicios/mascarilla.html', {})
# Productos
def pomada(request):
    return render(request, 'productos/pomada.html', {})

def after(request):
    return render(request, 'productos/after.html', {})

def shampoo(request):
    return render(request, 'productos/shampoo.html', {})

def aceites(request):
    return render(request, 'productos/aceites.html', {})

def talco(request):
    return render(request, 'productos/talco.html', {})
# Contacto
def citas(request):
    return render(request, 'contacto/citas.html', {})

def redes(request):
    return render(request, 'contacto/redes.html', {})

def mensaje(request):
    return render(request, 'contacto/mensaje.html', {})

def ubicacion(request):
    return render(request, 'contacto/ubicacion.html', {})
# Forms get started sing in
def formStart(request):
    return render(request, 'forms/formStart.html', {})

def formSing(request):
    return render(request, 'forms/formSing.html', {})

# Vistas de los formularios.

def citaSuccess(request):
    name = request.POST['name']
    return render(request, 'citaSuccess.html', {"name": name})

def inicioSuccess(request):
    if request.method != 'POST':
        return HttpResponse("El metodo GET no est soportado por esta ruta")
    info = request.POST['info']
    return render(request, 'inicioSuccess.html', {"info": info})
    
def startSuccess(request):
    if request.method != 'POST':
        return HttpResponse("El metodo GET no est soportado por esta ruta")
    name2 = request.POST['name2']
    return render(request, 'startSuccess.html', {"name2": name2})

# Vistas de parte legal
def terminos(request):
    return render(request, 'terminos.html', {})

def aviso(request):
    return render(request, 'aviso.html', {})