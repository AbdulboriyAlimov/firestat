# Generated by Django 4.0.3 on 2022-04-18 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eguide', '0002_object_registration_obj_antifire_machine_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='object_registration',
            name='obj_Guilty_Person_Age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='object_registration',
            name='obj_Object_Name',
            field=models.CharField(default='None', max_length=250),
        ),
    ]
