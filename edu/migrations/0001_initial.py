# Generated by Django 4.0.6 on 2022-09-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Educational',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(max_length=100)),
                ('board1', models.CharField(max_length=100)),
                ('board2', models.CharField(max_length=100)),
                ('passing_year', models.PositiveBigIntegerField()),
                ('passing_year1', models.PositiveBigIntegerField()),
                ('passing_year2', models.PositiveBigIntegerField()),
                ('percentage', models.CharField(max_length=100)),
                ('percentage1', models.CharField(max_length=100)),
                ('percentage2', models.CharField(max_length=100)),
                ('roll_number', models.PositiveBigIntegerField()),
                ('roll_number1', models.PositiveBigIntegerField()),
                ('roll_number2', models.PositiveBigIntegerField()),
                ('course_applied_for', models.CharField(choices=[('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th,', '10th'), ('11th', '11th'), ('12th', '12th'), ('Graduation', 'Graduation'), ('Special Classes', 'Special Clases'), ('DCA', 'DCA'), ('CFA', 'CFA'), ('DDTP', 'DDTP'), ('DCAD', 'DCAD'), ('ADCA', 'ADCA'), ('DCP', 'DCP'), ('HDCA', 'HDCA'), ('DAP', 'DAP'), ('HDAP', 'HDAP'), ('HDIT', 'HDIT'), ('ADIT', 'ADIT'), ('DCH', 'DCH'), ('ADCHN', 'ADCHN'), ('DCN', 'DWD'), ('DWD', 'DWD'), ('DMM', 'DMM'), ('ADGA', 'ADGA'), ('DCT', 'DCT'), ('DOM', 'DOM'), ('DMR', 'DMR'), ('DID', 'DID'), ('Professional Courses', 'Professional Courses')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Persional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('fathername', models.CharField(max_length=100)),
                ('mothername', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('Andman & Nicobar Island', 'Andman & Nicobar Island'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujrat', 'Gujrat'), ('Haryana', 'Hryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kasmir', 'Jammu & Kasmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerla', 'Kerla'), ('Lakshadweep', 'Lakshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalay', 'Meghalay'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajsthan', 'Rajsthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal')], max_length=25)),
                ('pin', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UploadDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photoimage')),
                ('signature', models.ImageField(blank=True, upload_to='signatureimage')),
                ('matriculation', models.FileField(blank=True, upload_to='matricdoc')),
                ('intermediate', models.FileField(blank=True, upload_to='intermediatedoc')),
                ('graducation', models.FileField(blank=True, upload_to='graducationdoc')),
                ('postgraducation', models.FileField(blank=True, upload_to='postgraducationdoc')),
                ('address_proof', models.FileField(blank=True, upload_to='photodoc')),
            ],
        ),
    ]
