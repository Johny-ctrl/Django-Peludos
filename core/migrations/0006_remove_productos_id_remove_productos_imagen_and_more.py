# Generated by Django 4.0.5 on 2022-06-04 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_productos_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='id',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='nombre',
        ),
        migrations.AddField(
            model_name='productos',
            name='IdProducto',
            field=models.CharField(default=1, max_length=45, primary_key=True, serialize=False, verbose_name='Id del producto'),
            preserve_default=False,
        ),
    ]
