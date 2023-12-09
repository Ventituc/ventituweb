# Generated by Django 4.2.8 on 2023-12-09 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fechaInsgreso', models.DateField()),
                ('ingresodiaLaboral', models.BooleanField()),
                ('fechaingLocal', models.DateField()),
                ('codigoQr', models.CharField(max_length=200)),
                ('reingreso', models.BooleanField()),
                ('fotoDelantera', models.ImageField(upload_to='')),
                ('fotoTrasera', models.ImageField(upload_to='')),
                ('fotoSticker', models.ImageField(upload_to='')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('pulgadas', models.IntegerField()),
                ('codModelo', models.CharField(max_length=150)),
                ('descripcionModelo', models.TextField(blank=True, null=True)),
                ('condicion', models.CharField(max_length=100)),
                ('fechaSticker', models.DateField()),
                ('nombreSticker', models.CharField(max_length=100)),
                ('codigoSticker', models.FloatField(blank=True, null=True)),
                ('garantia', models.CharField(max_length=50)),
                ('inicioDiagnostico', models.DateTimeField()),
                ('diagnosticoTecnico', models.TextField(blank=True, null=True)),
                ('presupuestado', models.BooleanField()),
                ('description', models.TextField(blank=True, null=True)),
                ('estadoPresupuesto', models.CharField(max_length=50)),
                ('fechaAprobacion', models.DateField()),
                ('inicioReparacion', models.DateTimeField()),
                ('tipoReparacion', models.CharField(max_length=50)),
                ('capUsado', models.CharField(max_length=100)),
                ('bujes', models.CharField(max_length=100)),
                ('repuestosUsados', models.TextField(blank=True, null=True)),
                ('motor', models.CharField(max_length=50)),
                ('codMotor', models.CharField(max_length=100)),
                ('finalReparacion', models.DateTimeField()),
                ('resumenGeneral', models.TextField(blank=True, null=True)),
                ('fechaSalida', models.DateField()),
                ('fotoSalida', models.ImageField(upload_to='')),
                ('estadoActual', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms_as_host', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL)),
                ('responsableDiagnostico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms_as_diagnostic_responsible', to=settings.AUTH_USER_MODEL)),
                ('responsableReparacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms_as_repair_responsible', to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.topic')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]