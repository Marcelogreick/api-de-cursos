# Generated by Django 2.2.9 on 2020-11-02 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('comments', models.TextField(blank=True, default='')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='curso.Curso')),
            ],
            options={
                'verbose_name': 'rating',
                'verbose_name_plural': 'ratings',
                'unique_together': {('email', 'curso')},
            },
        ),
    ]
