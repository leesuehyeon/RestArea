# Generated by Django 4.2.4 on 2023-08-11 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.review')),
            ],
        ),
    ]
