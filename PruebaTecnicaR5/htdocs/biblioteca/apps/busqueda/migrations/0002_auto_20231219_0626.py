# Generated by Django 3.1.3 on 2023-12-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='categoria',
        ),
        migrations.AlterField(
            model_name='autores',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categorias',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='libro',
            name='Descripcion',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='libro',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='libro',
            name='Imagen',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='libro',
            name='Subtitulo',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
