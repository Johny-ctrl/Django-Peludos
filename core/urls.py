
from django.urls import path
from .views import home, Productos,Formulario, form_productos,form_mod_productos,del_producto

urlpatterns = [
    path('', home,name="home"),
    path('productos',Productos,name="Productos"), 
    path('Formulario',Formulario, name='Formulario'),
    path('form-productos',form_productos, name='form_productos'),
    path('form-mod-productos/<ID>',form_mod_productos, name='form_mod_productos'),
    path('del_producto/<ID>',del_producto, name='del_producto'),
]
