# Generated by Django 4.1.4 on 2023-04-23 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0011_rename_amount_admission_status_payment_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission_status',
            old_name='payment_id',
            new_name='reg_amount',
        ),
    ]
