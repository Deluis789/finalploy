# Generated by Django 4.2 on 2024-11-11 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Urbanizaciones',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('field_gid', models.DecimalField(blank=True, db_column='__gid', decimal_places=0, max_digits=10, null=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('c_dist_mun', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('rta', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_rta', models.CharField(blank=True, max_length=15, null=True)),
                ('rm', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_rm', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_aniv', models.CharField(blank=True, max_length=50, null=True)),
                ('nom_presid', models.CharField(blank=True, max_length=50, null=True)),
                ('poblacion', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('obs', models.CharField(blank=True, max_length=100, null=True)),
                ('gid_urb', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('area_m2', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('geom', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'urbanizaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CalleAv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Calle/Avenida',
                'verbose_name_plural': 'Calles/Avenidas',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('ci', models.CharField(max_length=10)),
                ('numero_vivienda', models.CharField(max_length=10)),
                ('codigo_usuario', models.CharField(blank=True, max_length=6, null=True, unique=True)),
                ('calle_av', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.calleav')),
                ('rol', models.ManyToManyField(blank=True, to='auth.group')),
                ('urbanizaciones', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.urbanizaciones')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudVecino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_vecino', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('distrito', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('ubicacion_geografica', models.CharField(help_text='Formato: Latitud, Longitud', max_length=100)),
                ('foto', models.ImageField(upload_to='imagenes_vecinos/')),
                ('nombres', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('cedula_identidad', models.CharField(max_length=20, unique=True)),
                ('celular', models.CharField(max_length=15)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('urbanizaciones', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.urbanizaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distrito', models.CharField(blank=True, max_length=10, null=True)),
                ('ubicacion_geografica', models.CharField(help_text='Formato: Latitud, Longitud', max_length=100)),
                ('nombres', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('cedula_identidad', models.CharField(max_length=20, unique=True)),
                ('estado', models.CharField(choices=[('realizado', 'Realizado'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado'), ('desecho', 'Desecho')], max_length=50)),
                ('codigo_vecino', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.solicitudvecino')),
                ('designacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='solicitud_designacion', to=settings.AUTH_USER_MODEL)),
                ('urbanizaciones', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.urbanizaciones')),
            ],
        ),
        migrations.CreateModel(
            name='FichaOperativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('distrito', models.CharField(max_length=10)),
                ('urbanizacion', models.CharField(max_length=100)),
                ('latitud_longitud', models.CharField(help_text='Formato: Latitud, Longitud', max_length=100)),
                ('tecnico', models.CharField(max_length=50)),
                ('ubicacion_direccion', models.CharField(max_length=100)),
                ('cuadrilla', models.CharField(max_length=100)),
                ('maquinaria', models.CharField(blank=True, max_length=100, null=True)),
                ('operador', models.CharField(blank=True, max_length=100, null=True)),
                ('concepto', models.CharField(max_length=100)),
                ('volumen', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('fotoInicio', models.ImageField(upload_to='fichas_operativas/')),
                ('fotoDesarollo', models.ImageField(upload_to='fichas_operativas/')),
                ('fotoCulminado', models.ImageField(upload_to='fichas_operativas/')),
                ('estado', models.CharField(choices=[('finalizado', 'Finalizado'), ('proceso', 'En proceso'), ('abandono', 'Abandonado')], max_length=50)),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.solicitudes')),
            ],
        ),
    ]
