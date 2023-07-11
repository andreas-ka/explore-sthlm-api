# Generated by Django 3.2.20 on 2023-07-11 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Sport', 'Sport'), ('Music', 'Music'), ('Culture', 'Culture'), ('Family', 'Family'), ('Food', 'Food'), ('Shopping', 'Shopping'), ('Sightseeing', 'Sightseeing')], default='', max_length=255),
        ),
    ]
