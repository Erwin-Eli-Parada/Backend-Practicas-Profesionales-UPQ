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
        return self.nombre +" "+str(self.id_asesor)
    

# Modelo de Empresa
class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key = True)
    nombre_empresa = models.CharField('nombre_empresa',max_length=200,blank=False,null=False)
    sector = models.CharField('sector',max_length=100,blank=True,null=False)
    giro = models.CharField('giro',max_length=100,blank=True,null=False)
    tamanio = models.CharField('tamanio',max_length=2,blank=True,null=False)
    correo = models.CharField('correo',max_length=200,blank=True,null=False)
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
    id_asesor_ext = models.ForeignKey(AsesorExterno, on_delete=models.CASCADE, related_name='encuesta')

    class Meta:
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuestas'

    def __str__(self):
        return self.descripcion + self.valor_descripcion
    
# Modelo Estatus de la residencia
class EstatusResidencia(models.Model):
    id_practica = models.IntegerField(primary_key = True)
    comentarios_status = models.CharField('comentarios_status',max_length=1000,blank=True,null=False)
    estatus_proceso = models.CharField('estatus_proceso',max_length=100,blank=True,null=False)
    tipo_proceso = models.CharField('tipo_proceso',max_length=100,blank=False,null=False)
    carta_recibida = models.BooleanField(default=False)
    avance_1 = models.BooleanField(default=False)
    avance_2 = models.BooleanField(default=False)
    reporte_final = models.BooleanField(default=False)
    carta_liberacion = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Residencia'
        verbose_name_plural = 'Residencias'

    def __str__(self):
        return self.comentarios_status

# Modelo de proyecto
class Proyecto(models.Model):
    id_practica = models.OneToOneField(EstatusResidencia, on_delete=models.CASCADE, verbose_name='Practica', null=False)
    nombre_proyecto = models.CharField('nombre_proyecto',max_length=300,blank=True,null=False)
    fecha_solicitud = models.DateTimeField('Fecha de eliminacion',blank=True, null=True)
    metodo_conocimiento = models.CharField('metodo_conocimiento',max_length=100,blank=True,null=False)
    calificacion = models.DecimalField('calificacion',max_digits=5,decimal_places=2,blank=True)
    comentarios_finales = models.CharField('comentarios_finales',max_length=400,blank=True,null=False)
    id_asesor = models.ForeignKey(AsesorUPQ, on_delete=models.CASCADE, verbose_name='Asesor UPQ')
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')
    id_asesor_ext = models.ForeignKey(AsesorExterno, on_delete=models.CASCADE, verbose_name='Asesor Externo', null=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.nombre_proyecto

# Modelo del alumno
class Alumno(models.Model):
    matricula = models.CharField(primary_key = True, max_length=10)
    correo = models.EmailField('correo',max_length=200,blank=True,null=False)
    correo_institucional = models.EmailField('correo_institucional',max_length=200,blank=True,null=False)
    generacion = models.IntegerField(blank=False,null=False)
    grupo = models.CharField('grupo',max_length=10,blank=False,null=False)
    carrera = models.CharField('carrera',max_length=50,blank=False,null=False)
    nss = models.CharField('nss',max_length=50,blank=False,null=False)
    genero = models.CharField('genero',max_length=50,blank=False,null=False)
    nombre = models.CharField('nombre',max_length=100,blank=False,null=False)
    id_practica = models.ForeignKey(Proyecto, on_delete=models.CASCADE, verbose_name='Proyecto')

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        return self.nombre
