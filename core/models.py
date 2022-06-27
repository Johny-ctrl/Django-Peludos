
from django.db import models
from pyexpat import model


# Create your models here.
class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria=models.CharField(max_length=50, verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria

class ListaP(models.Model):
    IdProducto=models.CharField(max_length=45,primary_key=True, verbose_name='Id del producto')
    NombreP= models.CharField(max_length=25, verbose_name='Nombre Producto')
    Imagen= models.ImageField(upload_to="ImgProductos", null=True)
    Descripcion= models.TextField(max_length=300, verbose_name='Descripcion Producto')
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Precio = models.IntegerField(verbose_name='Precio')
    def __str__(self):
        return self.IdProducto 