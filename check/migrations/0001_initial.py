# Generated by Django 4.2.4 on 2023-08-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_1', models.TextField(choices=[('포털사이트', '포털사이트'), ('지인 추천', '지인 추천'), ('Sns', 'Sns'), ('주소직접 입력', '주소직접 입력'), ('기타', '기타')], default='포털사이트', max_length=20)),
                ('score_2', models.TextField(choices=[('매우만족', '매우만족'), ('만족', '만족'), ('보통', '보통'), ('불만족', '불만족'), ('매우 불만족', '매우 불만족')], default='매우만족', max_length=20)),
                ('content_1', models.TextField()),
                ('content_2', models.TextField()),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
