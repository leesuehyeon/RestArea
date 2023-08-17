# Generated by Django 4.2.4 on 2023-08-13 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_alter_review_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.CharField(choices=[('평점: (1/5)', '1'), ('평점: (2/5)', '2'), ('평점: (3/5)', '3'), ('평점: (4/5)', '4'), ('평점: (5/5)', '5')], default='평점: (5/5)', max_length=20),
        ),
    ]
