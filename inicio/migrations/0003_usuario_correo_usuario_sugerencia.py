# Generated by Django 5.0.6 on 2024-06-13 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_usuario_delete_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='sugerencia',
            field=models.CharField(default=3, max_length=20),
            preserve_default=False,
        ),
    ]
