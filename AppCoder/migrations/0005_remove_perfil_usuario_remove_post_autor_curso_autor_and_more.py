# Generated by Django 4.2.7 on 2023-12-23 20:47

import AppCoder.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppCoder', '0004_post_perfil_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='post',
            name='autor',
        ),
        migrations.AddField(
            model_name='curso',
            name='autor',
            field=models.ForeignKey(default=AppCoder.models.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='post'),
        ),
        migrations.AddField(
            model_name='curso',
            name='subtitulo',
            field=models.CharField(default='Subtítulo por defecto', max_length=100),
        ),
        migrations.AlterField(
            model_name='curso',
            name='post',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]