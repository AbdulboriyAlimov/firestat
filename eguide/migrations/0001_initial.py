# Generated by Django 4.0.3 on 2022-04-17 08:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='antifire_Machine_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antifire_Machine_Code', models.IntegerField(default=0)),
                ('antifire_Machine_Type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='antifire_People_Attended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended_People_Code', models.IntegerField(default=0)),
                ('attended_People', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='building_Antifire_Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ats_Name', models.CharField(max_length=250, unique=True)),
                ('ats_Added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='building_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bld_Type', models.CharField(max_length=250, unique=True)),
                ('bld_Added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='causing_To_Death_Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('death_Condition_Code', models.IntegerField(default=0)),
                ('death_Condition_Cause', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_Code', models.IntegerField(unique=True)),
                ('city_Name', models.CharField(max_length=250, unique=True)),
                ('city_Added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='commercial_Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corg_Code', models.IntegerField(default=0)),
                ('corg_Name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='dead_Degree_Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_Code', models.IntegerField(default=0)),
                ('degree_Type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='dead_Family_Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_Code', models.IntegerField(default=0)),
                ('family_Condition', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='dead_Gender_Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender_Code', models.IntegerField(default=0)),
                ('gender_Type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='dead_Social_Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_Condition_Code', models.IntegerField(default=0)),
                ('social_Condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='death_Reason_In_Fire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('death_Reason_Code', models.IntegerField(default=0)),
                ('people_Death_Reason', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='death_Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('death_Moment_Code', models.IntegerField(default=0)),
                ('death_Moment_Time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='dist_Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_Code', models.IntegerField(default=0, unique=True)),
                ('org_Name', models.CharField(max_length=250, unique=True)),
                ('org_Added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='fire_Event_Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fire_Event_Location_Code', models.IntegerField(default=0)),
                ('fire_Event_Location_Name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='fire_Event_Location_Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('construction_Code', models.IntegerField(default=0)),
                ('construction_Element', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='fire_Extinguisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extinguisher_Code', models.IntegerField(default=0)),
                ('extinguisher_Type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='fire_Floor_Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_Code', models.IntegerField(default=0)),
                ('floor_Type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='fire_guilty_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guilty_Category_Code', models.IntegerField(default=0)),
                ('guilty_Person', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='fire_Investigation_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investigation_Result_Code', models.IntegerField(default=0)),
                ('investigation_Result', models.CharField(max_length=250)),
                ('alleged_By', models.CharField(max_length=250)),
                ('criminal_Article_Of_RUz', models.CharField(max_length=250)),
                ('adminisitrative_Responsibility', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='fire_Objects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fire_Object_Code', models.IntegerField(default=0)),
                ('fire_Object_Purpose', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='fire_Pistols',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pistol_Code', models.IntegerField(default=0)),
                ('pistol_type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='fire_Resistance_Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resistance_Code', models.IntegerField(default=0)),
                ('resistance_Level', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='fire_Source_Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_Element_Code', models.IntegerField(default=0)),
                ('source_Element_Name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Источник возникновения пожара',
                'verbose_name_plural': 'Источник возникновения пожара',
            },
        ),
        migrations.CreateModel(
            name='fire_Widespread_Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition_Code', models.IntegerField(default=0)),
                ('condition_Source', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='guilty_Person_Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guilty_Person_Condition_Code', models.IntegerField(default=0)),
                ('guilty_Condition', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='guilty_Person_Relation_To_Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guilty_Person_Relation_Code', models.IntegerField(default=0)),
                ('guilty_Person_Relation', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='head_Of_Antifire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_Code', models.IntegerField(default=0)),
                ('head_Name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='injured_Person_Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('injured_Code', models.IntegerField(default=0)),
                ('injured_Gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='machines_Used_Antifire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_Code', models.IntegerField(default=0)),
                ('machine_Type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ministery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ministery_Code', models.IntegerField(default=0)),
                ('ministery_Name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='object_Securit_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_Security_Code', models.IntegerField(default=0)),
                ('object_Security_Name', models.CharField(max_length=250, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='object_Transport_Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_Transport_Condition_Code', models.IntegerField(default=0)),
                ('object_Transport_Condition_Type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='OOG_Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_Code', models.IntegerField(default=0)),
                ('OOG_Departure_Group', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='organisation_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organ_Code', models.IntegerField(default=0)),
                ('organ_Name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='primary_Antifire_Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_Source_Code', models.IntegerField(default=0)),
                ('primary_Antifire_Source_Type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='primary_Source_Usage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_Usage_Code', models.IntegerField(default=0)),
                ('source_Usage_Type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='property_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_Type', models.CharField(max_length=250, unique=True)),
                ('property_Added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_Code', models.IntegerField(default=0)),
                ('region_Name', models.CharField(max_length=250, unique=True)),
                ('region_Added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='result_Of_Antifire_Machine_Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antifire_Machine_Work_Code', models.IntegerField(default=0)),
                ('result_Antifire_Machine_Work', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='water_Source_Usage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_Usage_Code', models.IntegerField(default=0)),
                ('water_Usage_Purpose', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='water_Supply_Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_Supply_Code', models.IntegerField(default=0)),
                ('water_Supply_Type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='object_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_Fire_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('obj_Building_Antifire_Service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eguide.building_antifire_service')),
                ('obj_Building_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eguide.building_type')),
                ('obj_City', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eguide.city', to_field='city_Code')),
                ('obj_Commercial_Organisation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eguide.commercial_organisation')),
                ('obj_Fire_Objects', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eguide.fire_objects')),
                ('obj_Ministery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eguide.ministery')),
                ('obj_Org_Code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eguide.dist_organisation')),
                ('obj_Organisation_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eguide.organisation_name')),
                ('obj_Property_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eguide.property_type')),
                ('obj_Region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eguide.region')),
                ('obj_Security_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eguide.object_securit_type')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='region_Code1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eguide.region'),
        ),
    ]
