from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # Servicios
    path('cortes', views.cortes, name='cortes'),
    path('barba', views.barba, name='barba'),
    path('contornos', views.contornos, name='contornos'),
    path('ceja', views.ceja, name='ceja'),
    path('mascarilla', views.mascarilla, name='mascarilla'),
    # Productos
    path('pomada', views.pomada, name='pomada'),
    path('after', views.after, name='after'),
    path('shampoo', views.shampoo, name='shampoo'),
    path('aceites', views.aceites, name='aceites'),
    path('talco', views.talco, name='talco'),
    # Contacto
    path('citas', views.citas, name='citas'),
    path('redes', views.redes, name='redes'),
    path('mensaje', views.mensaje, name='mensaje'),
    path('ubicacion', views.ubicacion, name='ubicacion'),
    # Forms get started sing in
    path('formStart', views.formStart, name='formStart'),
    path('formSing', views.formSing, name='formSing'),
]