# Generated by Django 4.1.4 on 2023-02-25 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0002_addmissionform_admission_details_payment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission_details',
            old_name='amount',
            new_name='payment_id',
        ),
        migrations.AlterField(
            model_name='admission_details',
            name='admission_status',
            field=models.CharField(choices=[('Payment_Not_Completed', 'Payment_Not_completed'), ('Accepted', 'Accepted'), ('Succsess', 'Succsess'), ('Cancel', 'Cancel')], default='Pending', max_length=50),
        ),
    ]