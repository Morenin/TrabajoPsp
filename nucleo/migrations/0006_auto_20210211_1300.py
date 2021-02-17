# Generated by Django 2.1.5 on 2021-02-11 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0005_auto_20210209_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reparacion',
            name='Id_Mecanico',
        ),
        migrations.AddField(
            model_name='reparacion',
            name='Pendiente',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='coche',
            name='Cliente_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='Id_Mecanico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='Id_Cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Mecanico',
        ),
    ]
