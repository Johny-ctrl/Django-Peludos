# Generated by Django 4.0.5 on 2022-06-04 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_productos_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='nombre',
            field=models.CharField(default=1, max_length=25, verbose_name='Nombre Producto'),
            preserve_default=False,
        ),
    ]