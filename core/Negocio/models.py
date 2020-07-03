from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)
    def __str__(self):
        return '{}'.format(self.nombre)

class Direccion(models.Model):
    calle = models.CharField(max_length=20)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=20)
    def __str__(self):
        return '{}'.format(self.calle)

class Proveedor(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    web = models.CharField(max_length=40)
    def __str__(self):
        return '{}'.format(self.nombre)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio = models.IntegerField()
    stock = models.IntegerField()
    def __str__(self):
        return '{}'.format(self.nombre)

class Detalle(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    def __str__(self):
        return '{}'.format(self.producto)

class Cliente(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    detalle = models.ManyToManyField(Detalle)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto = models.IntegerField()
    descuento = models.BooleanField()
    def __str__(self):
        return '{}'.format(self.id)


