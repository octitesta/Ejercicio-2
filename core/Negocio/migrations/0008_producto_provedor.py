# Generated by Django 2.2 on 2020-06-25 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Negocio', '0007_proveedor_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='provedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Negocio.Proveedor'),
            preserve_default=False,
        ),
    ]
