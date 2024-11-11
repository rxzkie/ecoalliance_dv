from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('nombre',)
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Productos(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='uploads/', blank=True, null=True)
    miniatura = models.ImageField(upload_to='uploads/', blank=True, null=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-fecha_agregado',)
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return f'/{self.categoria.slug}/{self.slug}/'
    
    def get_imagen(self):
        if self.imagen:
            return self.imagen.url
        return ''
    
    def get_miniatura(self):
        if self.miniatura:
            return self.miniatura.url
        elif self.imagen:
            self.miniatura = self.crear_miniatura(self.imagen)
            self.save()
            return self.miniatura.url
        return ''
    
    def crear_miniatura(self, imagen, tamaño=(300, 200)):
        img = Image.open(imagen)
        img.convert('RGB')
        img.thumbnail(tamaño)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        miniatura = File(thumb_io, name=imagen.name)

        return miniatura
