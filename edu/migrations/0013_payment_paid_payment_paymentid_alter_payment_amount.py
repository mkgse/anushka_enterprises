# Generated by Django 4.0.2 on 2023-05-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0012_rename_payment_id_admission_status_reg_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payment',
            name='paymentid',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.CharField(max_length=100),
        ),
    ]
