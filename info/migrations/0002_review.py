# Generated by Django 4.2.4 on 2023-08-09 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date', models.DateTimeField()),
                ('restreview', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='info.info')),
            ],
        ),
    ]
