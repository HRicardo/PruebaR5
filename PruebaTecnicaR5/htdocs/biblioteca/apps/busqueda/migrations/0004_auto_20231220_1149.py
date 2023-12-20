# Generated by Django 3.1.3 on 2023-12-20 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0003_auto_20231219_0633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autores',
            name='Libro_id',
        ),
        migrations.RemoveField(
            model_name='categorias',
            name='Libro_id',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='categoria',
        ),
        migrations.CreateModel(
            name='tablaIntermediaCategorias',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busqueda.categorias')),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busqueda.libro')),
            ],
        ),
        migrations.CreateModel(
            name='tablaIntermediaAutores',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busqueda.autores')),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busqueda.libro')),
            ],
        ),
    ]
