# Generated by Django 4.2.4 on 2023-08-14 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_alter_info_voter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
