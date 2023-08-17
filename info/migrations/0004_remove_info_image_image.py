# Generated by Django 4.2.4 on 2023-08-11 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_delete_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='image',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='info.info')),
            ],
        ),
    ]
