# Generated by Django 4.0.5 on 2022-07-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMVT', '0007_remove_auto_fechadefabricacion_remove_auto_servis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amigos',
            name='fechaDeNacimiento',
            field=models.CharField(max_length=10),
        ),
    ]
