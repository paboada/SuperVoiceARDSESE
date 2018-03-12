# Generated by Django 2.0.2 on 2018-02-19 03:20

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Concurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('valor_pagar', models.IntegerField()),
                ('ruta_imagen', models.ImageField(blank=True, null=True, upload_to='media')),
                ('texto_voz', models.CharField(max_length=2000)),
                ('recomendaciones', models.CharField(max_length=2000)),
                ('url_concurso', models.URLField(null=True)),
                ('url_concurso_custom', models.URLField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('estado', models.CharField(default='Vigente', max_length=2000, null=True)),
                ('id_administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Locutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('observaciones', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioCustom',
            fields=[
                ('id_administrador', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('Empresa', models.CharField(blank=True, max_length=200)),
                ('Rol', models.CharField(blank=True, choices=[('Administrador', 'Administrador'), ('Marketing', 'Marketing')], max_length=200)),
                ('first_name', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
