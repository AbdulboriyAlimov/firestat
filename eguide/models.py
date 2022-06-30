from ast import mod
from audioop import reverse
from email.policy import default
from django.db import models
from django.utils import timezone
from matplotlib.pyplot import cla

class Region(models.Model):
    region_Code = models.IntegerField(default=0)
    region_Name = models.CharField(max_length=250, unique=True,db_column='Наименование области')
    region_Added = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.region_Name
    class Meta:
        verbose_name = "Области"
        verbose_name_plural = "Области"

class City(models.Model):
    region_Code1 = models.ForeignKey(Region, 
    on_delete=models.CASCADE,null=True)
    city_Code = models.IntegerField(unique=True)
    city_Name = models.CharField(max_length=250, unique=True,db_column='Наименование города(райони)')
    city_Added = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.city_Name
    class Meta:
        verbose_name = "Города и районы"
        verbose_name_plural = "Города и районы"

class dist_Organisation(models.Model):
    org_Code = models.IntegerField(default=0, unique=True)
    org_Name = models.CharField(max_length=250, unique=True)
    org_Added = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.org_Name
    class Meta:
        verbose_name = "Орган ГПН ГСПБ"
        verbose_name_plural = "Орган ГПН ГСПБ"

class building_Type(models.Model):
    bld_Code = models.IntegerField
    bld_Type = models.CharField(max_length=250, unique=True, db_column='Вид населенного пункта')
    bld_Added = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return self.bld_Type
    class Meta:
        verbose_name = "Вид населенного пункта"
        verbose_name_plural = "Вид населенного пункта"

class building_Antifire_Service(models.Model):
    ats_Code = models.IntegerField
    ats_Name = models.CharField(max_length=250, unique=True)
    ats_Added = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.ats_Name
    class Meta:
        verbose_name = "Вид пожарной охраны населенного пункта"
        verbose_name_plural = "Вид пожарной охраны населенного пункта"

class property_Type(models.Model):
    property_Code = models.IntegerField
    property_Type = models.CharField(max_length=250, unique=True,db_column='Форма собственности')
    property_Added = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.property_Type
    class Meta:
        verbose_name = "Форма собственности обеъкта пожара"
        verbose_name_plural = "Форма собственности объекта пожара"

class commercial_Organisation(models.Model):
    corg_Code = models.IntegerField(default=0)
    corg_Name = models.CharField(max_length=250, unique=True,db_column='Наименование')

    def __str__(self) -> str:
        return self.corg_Name
    class Meta:
        verbose_name = "Организационно-правовая форма организации"
        verbose_name_plural = "Организационно-правовая форма организации"

class ministery(models.Model):
    ministery_Code = models.IntegerField(default=0)
    ministery_Name = models.CharField(max_length=250, unique=True,db_column='Наименование')

    def __str__(self) -> str:
        return self.ministery_Name
    class Meta:
        verbose_name = "Ведомственная принадлежность организации"
        verbose_name_plural = "Ведомственная принадлежность организации"

class organisation_name(models.Model):
    organ_Code = models.IntegerField(default=0)
    organ_Name = models.CharField(max_length=250, unique=True)

    def __str__(self) -> str:
        return self.organ_Name
    class Meta:
        verbose_name = "Тип предприятия,организации,учреждения"
        verbose_name_plural = "Тип предприятия,организации,учреждения"


class fire_Objects(models.Model):
    fire_Object_Code = models.IntegerField(default=0)
    fire_Object_Purpose = models.CharField(max_length=250, unique=True)

    def __str__(self) -> str:
        return self.fire_Object_Purpose
    class Meta:
        verbose_name = "Объект пожара"
        verbose_name_plural = "Объект пожара"

class object_Securit_Type(models.Model):
    object_Security_Code = models.IntegerField(default=0)
    object_Security_Name = models.CharField(max_length=250, null=True, unique=True,db_column='Наименование')

    def __str__(self) -> str:
        return self.object_Securit_Name
    class Meta:
        verbose_name = "Вид охраны объекта"
        verbose_name_plural = "Вид охраны объекта"

class object_Transport_Condition(models.Model):
    object_Transport_Condition_Code = models.IntegerField(default=0)
    object_Transport_Condition_Type = models.CharField(max_length=250,db_column='Транспорт')

    def __str__(self) -> str:
        return self.object_Transport_Condition_Type
    class Meta:
        verbose_name = "Состояние транспорта и новостройки"
        verbose_name_plural = "Состояние транспорта и новостройки"

class fire_Event_Location(models.Model):
    fire_Event_Location_Code = models.IntegerField(default=0)
    fire_Event_Location_Name = models.CharField(max_length=250,db_column='Наименование')

    def __str__(self) -> str:
        return self.fire_Event_Location_Name
    class Meta:
        verbose_name = "Место возникновение пожара"
        verbose_name_plural = "Место возникновение пожара"
    
class fire_Event_Location_Place(models.Model):
    construction_Code = models.IntegerField(default=0)
    construction_Element = models.CharField(max_length=250,db_column='Коструктивные элементы')

    def __str__(self) -> str:
        return self.construction_Element
    class Meta:
        verbose_name = "Место возникновение пожара-поле"
        verbose_name_plural = "Место возникновение пожара-поле"

class fire_Source_Element(models.Model):
    source_Element_Code = models.IntegerField(default=0)
    source_Element_Name = models.CharField(max_length=250,db_column='Наименование')

    def __str__(self) -> str:
        return self.source_Element_Name
    class Meta:
        verbose_name = "Источник возникновения пожара"
        verbose_name_plural = "Источник возникновения пожара"
class fire_Reason(models.Model):
    fire_Reason_Code = models.IntegerField(default=0)
    fire_Reason_Name = models.CharField(max_length=250,db_column='Наименование причины')

    def __str__(self) -> str:
        return self.fire_Reason_Name
    class Meta:
        verbose_name = "Причина пожара"
        verbose_name_plural = "Причина пожара"

class fire_guilty_category(models.Model):
    guilty_Category_Code = models.IntegerField(default=0)
    guilty_Person = models.CharField(max_length=250,db_column='Виновное лицо')

    def __str__(self) -> str:
        return self.guilty_Person
    class Meta:
        verbose_name = "Категория виновника пожара"
        verbose_name_plural = "Категория виновника пожара"
    
class guilty_Person_Relation_To_Object(models.Model):
    guilty_Person_Relation_Code = models.IntegerField(default=0)
    guilty_Person_Relation = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.guilty_Person_Relation
    class Meta:
        verbose_name = "Отношение виновного лица к объекту пожара"
        verbose_name_plural = "Отношение виновного лица к объекту пожара"
    
class guilty_Person_Condition(models.Model):
    guilty_Person_Condition_Code = models.IntegerField(default=0,db_column='Состояние')
    guilty_Condition = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.guilty_Condition
    class Meta:
        verbose_name = "Состояние виновного лица"
        verbose_name_plural = "Состояние виновного лица"
    
class fire_Investigation_Result(models.Model):
    investigation_Result_Code = models.IntegerField(default=0)
    investigation_Result = models.CharField(max_length=250,db_column='Результаты дознания')
    alleged_By = models.CharField(max_length=250,db_column='Кем возбуждено УД')
    criminal_Article_Of_RUz = models.CharField(max_length=250,db_column='Статьи УК Руз')
    adminisitrative_Responsibility = models.CharField(max_length=250,db_column='Админ, Ответственность') 

    def __str__(self) -> str:
        return self.investigation_Result
    class Meta:
        verbose_name = "Резулътат дознание по пожару"
        verbose_name_plural = "Резулътат дознание по пожару"
    
class fire_Floor_Number(models.Model):
    floor_Code = models.IntegerField(default=0)
    floor_Type = models.CharField(max_length=250,db_column='Этаж')

    def __str__(self) -> str:
        return self.floor_Type
    class Meta:
        verbose_name = "Этаж на котором возник пожар"
        verbose_name_plural = "Этаж на котором возник пожар"

class fire_Resistance_Level(models.Model):
    resistance_Code = models.IntegerField(default=0)
    resistance_Level = models.CharField(max_length=3,db_column='Степен огнестойкости')

    def __str__(self) -> str:
        return self.resistance_Level
    class Meta:
        verbose_name = "Степен огнестойкости"
        verbose_name_plural = "Степен огнестойкости"

class fire_Widespread_Condition(models.Model):
    condition_Code = models.IntegerField(default=0)
    condition_Source = models.CharField(max_length=250,db_column='Условие способствовавшие развитию пожара')

    def __str__(self) -> str:
        return self.condition_Source
    class Meta:
        verbose_name = "Условие способствовавшие развитию пожара"
        verbose_name_plural = "Условие способствовавшие развитию пожара"
    
class antifire_People_Attended(models.Model):
    attended_People_Code = models.IntegerField(default=0)
    attended_People = models.CharField(max_length=250,db_column='Участники тушения пожара')

    def __str__(self) -> str:
        return self.attended_People
    class Meta:
        verbose_name = "Участники тушения пожара"
        verbose_name_plural = "Участники тушения пожара"

class machines_Used_Antifire(models.Model):
    machine_Code = models.IntegerField(default=0)
    machine_Type = models.CharField(max_length=250,db_column='Вид пожарной техники')

    def __str__(self) -> str:
        return self.machine_Type
    class Meta:
        verbose_name = "Техника исползованная при тушении пожара"
        verbose_name_plural = "Техника исползованная при тушении пожара"

class fire_Pistols(models.Model):
    pistol_Code = models.IntegerField(default=0)
    pistol_type = models.CharField(max_length=250,db_column='Виж плжарного ствола')

    def __str__(self) -> str:
        return self.pistol_type
    class Meta:
        verbose_name = "Пожарные стволы"
        verbose_name_plural = "Пожарные стволы"

class fire_Extinguisher(models.Model):
    extinguisher_Code = models.IntegerField(default=0)
    extinguisher_Type = models.CharField(max_length=250,db_column='Огнетушительные вещества')

    def __str__(self) -> str:
        return self.extinguisher_Type
    class Meta:
        verbose_name = "Огнетушительные средства"
        verbose_name_plural = "Огнетушительные средства"

class primary_Antifire_Source(models.Model):
    primary_Source_Code = models.IntegerField(default=0)
    primary_Antifire_Source_Type = models.CharField(max_length=250,db_column='Первичные средств пожаротушения')

    def __str__(self) -> str:
        return self.primary_Antifire_Source_Type
    class Meta:
        verbose_name = "Первичные средств пожаротушения"
        verbose_name_plural = "Первичные средств пожаротушения"

class primary_Source_Usage(models.Model):
    source_Usage_Code = models.IntegerField(default=0)
    source_Usage_Type = models.CharField(max_length=250,db_column='Использование первичные средств')

    def __str__(self) -> str:
        return self.source_Usage_Type
    class Meta:
        verbose_name = "Использование первичные средств"
        verbose_name_plural = "Использование первичные средств"

class water_Supply_Source(models.Model):
    water_Supply_Code = models.IntegerField(default=0)
    water_Supply_Type = models.CharField(max_length=250,db_column='Вид источника')

    def __str__(self) -> str:
        return self.water_Supply_Type
    class Meta:
        verbose_name = "Водаснабжение на пожаре"
        verbose_name_plural = "Водаснабжение на пожаре"
    
class water_Source_Usage(models.Model):
    water_Usage_Code = models.IntegerField(default=0)
    water_Usage_Purpose = models.CharField(max_length=250,db_column='Использование водоисточника')

    def __str__(self) -> str:
        return self.water_Usage_Purpose
    class Meta:
        verbose_name = "Использование водоисточника"
        verbose_name_plural = "Использование водоисточника"

class antifire_Machine_Type(models.Model):
    antifire_Machine_Code = models.IntegerField(default=0)
    antifire_Machine_Type = models.CharField(max_length=250,db_column='Вид установки пожарной автоматики')

    def __str__(self) -> str:
        return self.antifire_Machine_Type
    class Meta:
        verbose_name = "Вид установки пожарной автоматики"
        verbose_name_plural = "Вид установки пожарной автоматики"
    
class result_Of_Antifire_Machine_Work(models.Model):
    antifire_Machine_Work_Code = models.IntegerField(default=0)
    result_Antifire_Machine_Work = models.CharField(max_length=250,db_column='Результаты работы')

    def __str__(self) -> str:
        return self.result_Antifire_Machine_Work
    class Meta:
        verbose_name = "Результаты работы установок пожарной автоматики"
        verbose_name_plural = "Результаты работы установок пожарной автоматики"

class head_Of_Antifire(models.Model):
    head_Code = models.IntegerField(default=0)
    head_Name = models.CharField(max_length=250,db_column='Руководителб тушение пожара')

    def __str__(self) -> str:
        return self.head_Name
    class Meta:
        verbose_name = "Руководителб тушение пожара"
        verbose_name_plural = "Руководителб тушение пожара"

class OOG_Departure(models.Model):
    departure_Code = models.IntegerField(default=0)
    OOG_Departure_Group = models.CharField(max_length=250,db_column='Выезд СОГ')

    def __str__(self) -> str:
        return self.OOG_Departure_Group
    class Meta:
        verbose_name = "Руководителб тушение пожара"
        verbose_name_plural = "Выезд следственно-оперативной группы"

class dead_Gender_Person(models.Model):
    gender_Code = models.IntegerField(default=0)
    gender_Type = models.CharField(max_length=50,db_column='Пол')

    def __str__(self) -> str:
        return self.gender_Type
    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Пол"

class dead_Social_Condition(models.Model):
    social_Condition_Code = models.IntegerField(default=0)
    social_Condition = models.CharField(max_length=100,db_column='Социальное положение')

    def __str__(self) -> str:
        return self.social_Condition
    class Meta:
        verbose_name = "Социальное положение погибшего при пожаре лица"
        verbose_name_plural = "Социальное положение погибшего при пожаре лица"

class dead_Family_Condition(models.Model):
    family_Code = models.IntegerField(default=0)
    family_Condition = models.CharField(max_length=250,db_column='Семейное положение')

    def __str__(self) -> str:
        return self.family_Condition
    class Meta:
        verbose_name = "Семейное положение погибшего при пожаре лица"
        verbose_name_plural = "Семейное положение погибшего при пожаре лица"

class dead_Degree_Level(models.Model):
    degree_Code = models.IntegerField(default=0)
    degree_Type = models.CharField(max_length=50,db_column='Образование')

    def __str__(self) -> str:
        return self.degree_Type
    class Meta:
        verbose_name = "Образование лица погибшего при пожаре"
        verbose_name_plural = "Образование лица погибшего при пожаре"

class death_Reason_In_Fire(models.Model):
    death_Reason_Code = models.IntegerField(default=0)
    people_Death_Reason = models.CharField(max_length=250,db_column='Причина гибели людей')

    def __str__(self) -> str:
        return self.people_Death_Reason
    class Meta:
        verbose_name = "Причина гибели людей при пожаре"
        verbose_name_plural = "Причина гибели людей при пожаре"

class causing_To_Death_Condition(models.Model):
    death_Condition_Code = models.IntegerField(default=0)
    death_Condition_Cause = models.CharField(max_length=250,db_column='Условие способствующие гибели')

    def __str__(self) -> str:
        return self.death_Condition_Cause
    class Meta:
        verbose_name = "Условие способствующие гибели и трамвиованию людей"
        verbose_name_plural = "Условие способствующие гибели и трамвиованию людей"

class death_Time(models.Model):
    death_Moment_Code = models.IntegerField(default=0)
    death_Moment_Time = models.DateTimeField(default=timezone.now,db_column='Момент наступление смерти')

    class Meta:
        verbose_name = "Момент наступление смерти"
        verbose_name_plural = "Момент наступление смерти"

class injured_Person_Gender(models.Model):
    injured_Code = models.IntegerField(default=0)
    injured_Gender = models.CharField(max_length=10,db_column='Пол')

    class Meta:
        verbose_name = "Пол трамвированного лица"
        verbose_name_plural = "Пол трамвированного лица"

class object_Registration(models.Model):
    #Obshie svedeniya
    obj_Region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True, blank=True)
    obj_City = models.ForeignKey(City,on_delete=models.CASCADE,to_field='city_Code',null=True, blank=True)
    obj_Org_Code = models.ForeignKey(dist_Organisation,on_delete=models.CASCADE,null=True, blank=True)
    obj_Fire_Date = models.DateTimeField(default=timezone.now, blank=True)
    obj_Building_Type = models.ForeignKey(building_Type,on_delete=models.CASCADE,null=True, blank=True)
    obj_Building_Antifire_Service = models.ForeignKey(building_Antifire_Service,on_delete=models.CASCADE,null=True, blank=True)
    #Obyekt pojara
    obj_Property_Type = models.ForeignKey(property_Type,on_delete=models.CASCADE,null=True, blank=True)
    obj_Commercial_Organisation = models.ForeignKey(commercial_Organisation,on_delete=models.CASCADE,null=True, blank=True)
    obj_Ministery = models.ForeignKey(ministery,on_delete=models.CASCADE,null=True, blank=True)
    obj_Organisation_Name = models.ForeignKey(organisation_name,on_delete=models.CASCADE, blank=True)
    obj_Fire_Objects = models.ForeignKey(fire_Objects,on_delete=models.CASCADE,null=True, blank=True)
    obj_Security_Type = models.ForeignKey(object_Securit_Type,on_delete=models.CASCADE,null=True, blank=True)
    obj_Object_Name = models.CharField(default='None',max_length=250, blank=True)
    obj_Transport_Condition = models.ForeignKey(object_Transport_Condition,on_delete=models.CASCADE,null=True, blank=True)
    obj_Fire_Event_Location = models.ForeignKey(fire_Event_Location,on_delete=models.CASCADE,null=True, blank=True)
    obj_Fire_Event_Location_Place = models.ForeignKey(fire_Event_Location_Place,on_delete=models.CASCADE,null=True, blank=True)
    obj_Fire_Source_Element = models.ForeignKey(fire_Source_Element,on_delete=models.CASCADE,null=True, blank=True)
    obj_Fire_Reason = models.ForeignKey(fire_Reason,on_delete=models.CASCADE,null=True, blank=True)
    obj_Fire_Guilty_Category = models.ForeignKey(fire_guilty_category,on_delete=models.CASCADE,null=True, blank=True)
    obj_Guilty_Person_Relation_To_Object = models.ForeignKey(guilty_Person_Relation_To_Object,on_delete=models.CASCADE,null=True, blank=True)
    obj_Guilty_Person_Condition = models.ForeignKey(guilty_Person_Condition,on_delete=models.CASCADE,null=True, blank=True)
    obj_Guilty_Person_Age = models.IntegerField(default=0, blank=True)
    obj_Fire_Investigation_Result = models.ForeignKey(fire_Investigation_Result,on_delete=models.CASCADE,null=True, blank=True)
    #Xarakteristika obyekta pojara
    obj_Fire_Floor_Number = models.ForeignKey(fire_Floor_Number,on_delete=models.CASCADE,null=True, blank=True)
    obj_Fire_Resistance_Level = models.ForeignKey(fire_Resistance_Level,on_delete=models.CASCADE,null=True, blank=True)
    obj_Fire_Widespread_Condition = models.ForeignKey(fire_Widespread_Condition,on_delete=models.CASCADE,null=True, blank=True)
    obj_Antifire_People_Attended = models.ForeignKey(antifire_People_Attended,on_delete=models.CASCADE,null=True, blank=True)
    obj_Machines_Used_Antifire = models.ForeignKey(machines_Used_Antifire,on_delete=models.CASCADE,null=True, blank=True)
    obj_Fire_Pistols = models.ForeignKey(fire_Pistols,on_delete=models.CASCADE,null=True, blank=True)
    obj_Fire_Extinguisher = models.ForeignKey(fire_Extinguisher,on_delete=models.CASCADE,null=True, blank=True)
    obj_Primary_Antifire_Source = models.ForeignKey(primary_Antifire_Source,on_delete=models.CASCADE,null=True, blank=True)
    obj_Primary_Source_Usage = models.ForeignKey(primary_Source_Usage,on_delete=models.CASCADE,null=True, blank=True)
    obj_Water_Supply_Source = models.ForeignKey(water_Supply_Source,on_delete=models.CASCADE,null=True, blank=True)
    obj_Water_Source_Usage = models.ForeignKey(water_Source_Usage,on_delete=models.CASCADE,null=True, blank=True)
    obj_Antifire_Machine_Type = models.ForeignKey(antifire_Machine_Type,on_delete=models.CASCADE,null=True, blank=True)
    obj_Result_Of_Antifire_Machine_Work = models.ForeignKey(result_Of_Antifire_Machine_Work,on_delete=models.CASCADE,null=True, blank=True)
    obj_Head_Of_Antifire = models.ForeignKey(head_Of_Antifire,on_delete=models.CASCADE,null=True, blank=True)
    obj_OOG_Departure = models.ForeignKey(OOG_Departure,on_delete=models.CASCADE,null=True, blank=True)
    obj_Dead_Gender_Person = models.ForeignKey(dead_Gender_Person,on_delete=models.CASCADE,null=True, blank=True)
    obj_Dead_Social_Condition = models.ForeignKey(dead_Social_Condition,on_delete=models.CASCADE,null=True, blank=True)
    obj_Dead_Family_Condition = models.ForeignKey(dead_Family_Condition,on_delete=models.CASCADE,null=True, blank=True)
    obj_Dead_Degree_Level = models.ForeignKey(dead_Degree_Level,on_delete=models.CASCADE,null=True, blank=True)
    obj_Death_Reason_In_Fire = models.ForeignKey(death_Reason_In_Fire,on_delete=models.CASCADE,null=True, blank=True)
    obj_Causing_To_Death_Condition = models.ForeignKey(causing_To_Death_Condition,on_delete=models.CASCADE,null=True, blank=True)
    obj_Death_Time = models.ForeignKey(death_Time,on_delete=models.CASCADE,null=True, blank=True)
    obj_Injured_Person_Gender = models.ForeignKey(injured_Person_Gender,on_delete=models.CASCADE,null=True, blank=True)
    
    def get_absolute_utl(self):
        return reverse('eguide:post_detail', args=[self.pk])
    
    class Meta:
        verbose_name = "Регистрация объекта"
        verbose_name_plural = "Регистрация объекта"