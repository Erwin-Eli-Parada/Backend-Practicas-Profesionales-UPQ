# Generated by Django 4.1.7 on 2023-05-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0004_alter_empresa_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='calificacion',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='calificacion'),
        ),
    ]
