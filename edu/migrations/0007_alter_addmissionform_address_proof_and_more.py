# Generated by Django 4.1.4 on 2023-04-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0006_alter_addmissionform_address_proof_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmissionform',
            name='address_proof',
            field=models.FileField(blank=True, upload_to='photodoc'),
        ),
        migrations.AlterField(
            model_name='addmissionform',
            name='graducation',
            field=models.FileField(blank=True, upload_to='graducationdoc'),
        ),
        migrations.AlterField(
            model_name='addmissionform',
            name='intermediate',
            field=models.FileField(blank=True, upload_to='intermediatedoc'),
        ),
        migrations.AlterField(
            model_name='addmissionform',
            name='matriculation',
            field=models.FileField(blank=True, upload_to='matricdoc'),
        ),
        migrations.AlterField(
            model_name='addmissionform',
            name='photo',
            field=models.ImageField(blank=True, default='photoimage/elon.jpg', upload_to='photoimage'),
        ),
        migrations.AlterField(
            model_name='addmissionform',
            name='postgraducation',
            field=models.FileField(blank=True, upload_to='postgraducationdoc'),
        ),
        migrations.AlterField(
            model_name='addmissionform',
            name='signature',
            field=models.ImageField(blank=True, upload_to='signatureimage'),
        ),
    ]
