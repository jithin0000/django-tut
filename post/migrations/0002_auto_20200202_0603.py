# Generated by Django 3.0.2 on 2020-02-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
