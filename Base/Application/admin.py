from django.contrib import admin
from .models import Producto, Carrito, ProductoP

# Register your models here.
admin.site.register(ProductoP)
admin.site.register(Producto)
admin.site.register(Carrito)