# Generated by Django 2.1.15 on 2021-03-26 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='time_minute',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]