# Generated by Django 3.1.3 on 2021-04-07 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_server_webApp', '0003_auto_20210407_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration_in_sec',
            field=models.IntegerField(default=0),
        ),
    ]
