# Generated by Django 3.2.9 on 2022-08-19 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20220819_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='codeLink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='liveLink',
            field=models.URLField(blank=True, null=True),
        ),
    ]
