# Generated by Django 4.0.4 on 2022-06-06 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_listap_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='listap',
            name='Precio',
            field=models.IntegerField(default=1, verbose_name='Precio'),
            preserve_default=False,
        ),
    ]