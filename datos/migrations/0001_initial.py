# Generated by Django 4.1.7 on 2023-04-26 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsesorExterno',
            fields=[
                ('id_asesor_ext', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_asesor_ext', models.CharField(max_length=200, verbose_name='nombre_asesor_ext')),
            ],
            options={
                'verbose_name': 'AsesorExterno',
                'verbose_name_plural': 'AsesoresExternos',
            },
        ),
        migrations.CreateModel(
            name='AsesorUPQ',
            fields=[
                ('id_asesor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'AsesorUPQ',
                'verbose_name_plural': 'AsesoresUPQ',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=200, verbose_name='nombre_empresa')),
                ('sector', models.CharField(blank=True, max_length=100, verbose_name='sector')),
                ('giro', models.CharField(blank=True, max_length=100, verbose_name='giro')),
                ('tamanio', models.CharField(blank=True, max_length=1, verbose_name='tamanio')),
                ('correo', models.EmailField(blank=True, max_length=200, verbose_name='correo')),
                ('telefono', models.CharField(blank=True, max_length=50, verbose_name='telefono')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id_practica', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_proyecto', models.CharField(max_length=300, verbose_name='nombre_proyecto')),
                ('fecha_solicitud', models.DateTimeField(verbose_name='Fecha de eliminacion')),
                ('metodo_conocimiento', models.CharField(blank=True, max_length=100, verbose_name='metodo_conocimiento')),
                ('calificacion', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='calificacion')),
                ('comentarios_finales', models.CharField(blank=True, max_length=400, verbose_name='comentarios_finales')),
                ('id_asesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.asesorupq', verbose_name='Asesor UPQ')),
                ('id_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.empresa', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='EstatusResidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentarios_status', models.CharField(blank=True, max_length=400, verbose_name='comentarios_status')),
                ('estatus_proceso', models.CharField(blank=True, max_length=100, verbose_name='estatus_proceso')),
                ('tipo_proceso', models.CharField(max_length=100, verbose_name='tipo_proceso')),
                ('carta_recibida', models.BooleanField(default=False)),
                ('avance_1', models.BooleanField(default=False)),
                ('avance_2', models.BooleanField(default=False)),
                ('reporte_final', models.BooleanField(default=False)),
                ('carta_liberacion', models.BooleanField(default=False)),
                ('id_practica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.proyecto', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Residencia',
                'verbose_name_plural': 'Residencias',
            },
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id_encuesta', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=300, verbose_name='descripcion')),
                ('valor_descripcion', models.CharField(max_length=100, verbose_name='valor_descripcion')),
                ('pregunta', models.CharField(max_length=300, verbose_name='pregunta')),
                ('valor', models.IntegerField()),
                ('id_asesor_ext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.asesorexterno', verbose_name='Asesor Externo')),
            ],
            options={
                'verbose_name': 'Encuesta',
                'verbose_name_plural': 'Encuestas',
            },
        ),
        migrations.AddField(
            model_name='asesorexterno',
            name='id_empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.empresa', verbose_name='Empresa'),
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('matricula', models.IntegerField(primary_key=True, serialize=False)),
                ('correo', models.EmailField(blank=True, max_length=200, verbose_name='correo')),
                ('correo_institucional', models.EmailField(blank=True, max_length=200, verbose_name='correo_institucional')),
                ('generacion', models.IntegerField()),
                ('grupo', models.CharField(max_length=10, verbose_name='grupo')),
                ('carrera', models.CharField(max_length=50, verbose_name='carrera')),
                ('nss', models.CharField(max_length=50, verbose_name='nss')),
                ('genero', models.CharField(max_length=50, verbose_name='genero')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('id_practica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.proyecto', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
    ]