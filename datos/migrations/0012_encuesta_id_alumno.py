# Generated by Django 4.1.7 on 2023-05-13 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0011_alter_encuesta_pregunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuesta',
            name='id_alumno',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='alumno'),
        ),
    ]
