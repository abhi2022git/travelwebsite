# Generated by Django 4.0.6 on 2022-08-04 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking_alter_search_search'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Book',
        ),
    ]
