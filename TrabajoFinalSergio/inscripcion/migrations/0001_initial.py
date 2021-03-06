# Generated by Django 2.1.5 on 2019-02-09 12:31

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
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('dni', models.CharField(max_length=100, verbose_name='DNI')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('cuenta_bancaria', models.CharField(max_length=200, verbose_name='Cuenta Bancaria')),
                ('cuota', models.IntegerField(default=30, verbose_name='Cuota')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Inscripción',
                'verbose_name_plural': 'Inscripciones',
                'ordering': ['created'],
            },
        ),
    ]
