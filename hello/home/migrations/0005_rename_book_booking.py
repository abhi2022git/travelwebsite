# Generated by Django 4.0.6 on 2022-08-04 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_booking_book'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Booking',
        ),
    ]
