# Generated by Django 3.0.5 on 2020-04-03 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlist',
            name='image',
            field=models.ImageField(default='', upload_to='events/images'),
        ),
    ]