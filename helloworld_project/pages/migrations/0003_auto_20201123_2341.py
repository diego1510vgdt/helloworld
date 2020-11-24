# Generated by Django 3.1.3 on 2020-11-23 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('contenido', models.CharField(max_length=200)),
                ('reccion', models.CharField(max_length=20)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.autor')),
            ],
        ),
        migrations.AlterField(
            model_name='publication',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='idPub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.publication'),
        ),
    ]
