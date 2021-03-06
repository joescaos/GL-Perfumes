# Generated by Django 3.0.7 on 2020-06-09 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('referencia', models.CharField(max_length=80)),
                ('imagen', models.ImageField(null=True, upload_to='perfume/')),
                ('precio', models.PositiveIntegerField()),
                ('Descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Perfume',
                'verbose_name_plural': 'Perfumes',
            },
        ),
    ]
