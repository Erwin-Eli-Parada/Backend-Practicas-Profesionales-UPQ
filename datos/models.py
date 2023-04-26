from django.db import models

# Create your models here.

# Modelo de asesor
class AsesorUPQ(models.Model):
    id_asesor = models.AutoField(primary_key = True)
    nombre = models.CharField('nombre',max_length=200,blank=False,null=False)

    class Meta:
        verbose_name = 'AsesorUPQ'
        verbose_name_plural = 'AsesoresUPQ'

    def __str__(self):
        return self.nombre + self.id_asesor
    

# Modelo de Empresa
class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key = True)
    nombre_empresa = models.CharField('nombre_empresa',max_length=200,blank=False,null=False)
    sector = models.CharField('sector',max_length=100,blank=True,null=False)
    giro = models.CharField('giro',max_length=100,blank=True,null=False)
    tamanio = models.CharField('tamanio',max_length=1,blank=True,null=False)
    correo = models.EmailField('correo',max_length=200,blank=True,null=False)
    telefono = models.CharField('telefono',max_length=50,blank=True,null=False)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre_empresa + self.sector
    
# Modelo de asesor externo
class AsesorExterno(models.Model):
    id_asesor_ext = models.AutoField(primary_key = True)
    nombre_asesor_ext = models.CharField('nombre_asesor_ext',max_length=200,blank=False,null=False)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    class Meta:
        verbose_name = 'AsesorExterno'
        verbose_name_plural = 'AsesoresExternos'

    def __str__(self):
        return self.nombre_asesor_ext + self.id_asesor_ext
    
# Modelo de Empresa
class Encuesta(models.Model):
    id_encuesta = models.AutoField(primary_key = True)
    descripcion = models.CharField('descripcion',max_length=300,blank=False,null=False)
    valor_descripcion = models.CharField('valor_descripcion',max_length=100,blank=False,null=False)
    pregunta = models.CharField('pregunta',max_length=300,blank=False,null=False)
    valor = models.IntegerField(blank=False,null=False)
    id_asesor_ext = models.ForeignKey(AsesorExterno, on_delete=models.CASCADE, verbose_name='Asesor Externo')

    class Meta:
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuestas'

    def __str__(self):
        return self.descripcion + self.valor_descripcion
    
