# Generated by Django 4.2.4 on 2023-09-25 18:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0004_usuarios_delete_clientes_delete_talleres'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Ingresa un número válido de 10 dígitos.', regex='^\\d{10}$')])),
                ('direccion', models.CharField(max_length=128)),
                ('cp', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(message='Ingresa un número válido de 5 dígitos.', regex='^\\d{5}$')])),
                ('calidad', models.IntegerField(default=0)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='usuarios',
        ),
    ]
