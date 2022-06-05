
from distutils.command.upload import upload
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import ListaP
from core.forms import ProductoForm
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):
  
    return render(request, 'core/home.html')

def Productos(request):
    #carga los datos
    productos=ListaP.objects.all()

    #Carga objeto al contexto
    contexto ={
        'productos' : productos
    }
    return render(request, 'core/Productos.html', contexto)
    
def Formulario(request):
  
    return render(request, 'core/Formulario.html')



def form_productos(request):

    contexto={
        'form': ProductoForm()
    }
    #Verificacion de peticion
    if request.method=='POST':

        #se recuperan los datos con request
        formulario=ProductoForm(request.POST)
        #validacion
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Guardado Correctamente"
    return render(request, 'core/form_productos.html', contexto)

#modificaion Producto
def form_mod_productos(request,ID):
    #se utilizara la id para modificar un producto
    producto = ListaP.objects.get(IdProducto = ID)
#se agrega contexto
    contexto = {
        'form': ProductoForm(instance=producto)
    }
    #Verificacion de peticion

    if request.method=='POST':
        #se recuperan los datos con request
        formulario = ProductoForm(data = request.POST , instance = producto)
        #validacion
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Modificado Correctamente"
    return render(request, 'core/form_mod_productos.html', contexto)


#eliminacion de producto

def del_producto(request, ID):
    #se usara la id para identificar el producto borrado
            producto = ListaP.objects.get(IdProducto = ID)
            #se elimina el producto que coincida con su id
            producto.delete()
            #redireccion a la pagina de productos
            return redirect(to= 'Productos')