# Generated by Django 3.0.8 on 2020-08-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_remove_contestant_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='image',
            field=models.ImageField(blank=True, upload_to='gallery'),
        ),
    ]