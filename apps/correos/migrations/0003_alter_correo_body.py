# Generated by Django 4.1.7 on 2023-03-30 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correos', '0002_alter_estado_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correo',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
