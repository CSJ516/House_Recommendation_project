# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cafe(models.Model):
    gid = models.AutoField(primary_key=True)
    house_type = models.CharField(max_length=254, blank=True, null=True)
    criteria = models.CharField(max_length=254, blank=True, null=True)
    con_name = models.CharField(max_length=254, blank=True, null=True)
    con_addres = models.CharField(max_length=254, blank=True, null=True)
    con_latitu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    con_longit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cafe'


class Convenience(models.Model):
    gid = models.AutoField(primary_key=True)
    house_type = models.CharField(max_length=254, blank=True, null=True)
    criteria = models.CharField(max_length=254, blank=True, null=True)
    con_name = models.CharField(max_length=254, blank=True, null=True)
    con_addres = models.CharField(max_length=254, blank=True, null=True)
    con_latitu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    con_longit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convenience'


class Culture(models.Model):
    gid = models.AutoField(primary_key=True)
    house_type = models.CharField(max_length=254, blank=True, null=True)
    criteria = models.CharField(max_length=254, blank=True, null=True)
    con_name = models.CharField(max_length=254, blank=True, null=True)
    con_addres = models.CharField(max_length=254, blank=True, null=True)
    con_latitu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    con_longit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'culture'


class Daiso(models.Model):
    gid = models.AutoField(primary_key=True)
    house_type = models.CharField(max_length=254, blank=True, null=True)
    criteria = models.CharField(max_length=254, blank=True, null=True)
    con_name = models.CharField(max_length=254, blank=True, null=True)
    con_addres = models.CharField(max_length=254, blank=True, null=True)
    con_latitu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    con_longit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daiso'

class Fastfood(models.Model):
    gid = models.AutoField(primary_key=True)
    house_type = models.CharField(max_length=254, blank=True, null=True)
    criteria = models.CharField(max_length=254, blank=True, null=True)
    con_name = models.CharField(max_length=254, blank=True, null=True)
    con_addres = models.CharField(max_length=254, blank=True, null=True)
    con_latitu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    con_longit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fastfood'


class Health(models.Model):
    gid = models.AutoField(primary_key=True)
    house_type = models.CharField(max_length=254, blank=True, null=True)
    criteria = models.CharField(max_length=254, blank=True, null=True)
    con_name = models.CharField(max_length=254, blank=True, null=True)
    con_addres = models.CharField(max_length=254, blank=True, null=True)
    con_latitu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    con_longit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'health'


class Hospital(models.Model):
    gid = models.AutoField(primary_key=True)
    house_type = models.CharField(max_length=254, blank=True, null=True)
    criteria = models.CharField(max_length=254, blank=True, null=True)
    con_name = models.CharField(max_length=254, blank=True, null=True)
    con_addres = models.CharField(max_length=254, blank=True, null=True)
    con_latitu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    con_longit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospital'


class Laundry(models.Model):
    gid = models.AutoField(primary_key=True)
    house_type = models.CharField(max_length=254, blank=True, null=True)
    criteria = models.CharField(max_length=254, blank=True, null=True)
    con_name = models.CharField(max_length=254, blank=True, null=True)
    con_addres = models.CharField(max_length=254, blank=True, null=True)
    con_latitu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    con_longit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laundry'


class Market(models.Model):
    gid = models.AutoField(primary_key=True)
    house_type = models.CharField(max_length=254, blank=True, null=True)
    criteria = models.CharField(max_length=254, blank=True, null=True)
    con_name = models.CharField(max_length=254, blank=True, null=True)
    con_addres = models.CharField(max_length=254, blank=True, null=True)
    con_latitu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    con_longit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market'


class NaverPropertyFinal(models.Model):
    gid = models.AutoField(primary_key=True)
    n_address = models.CharField(max_length=254, blank=True, null=True)
    n_rent = models.CharField(max_length=254, blank=True, null=True)
    n_size = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    n_size_pro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    n_deposit = models.BigIntegerField(blank=True, null=True)
    n_pay = models.BigIntegerField(blank=True, null=True)
    n_road = models.CharField(max_length=254, blank=True, null=True)
    n_name = models.CharField(max_length=254, blank=True, null=True)
    n_floor = models.CharField(max_length=254, blank=True, null=True)
    n_date = models.CharField(max_length=254, blank=True, null=True)
    n_latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    n_longitud = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    n_criteria = models.CharField(max_length=254, blank=True, null=True)
    n_loan = models.CharField(max_length=254, blank=True, null=True)
    n_side = models.CharField(max_length=254, blank=True, null=True)
    n_cost_inc = models.CharField(max_length=254, blank=True, null=True)
    n_cost = models.CharField(max_length=254, blank=True, null=True)
    n_double_f = models.CharField(max_length=254, blank=True, null=True)
    n_room_bat = models.CharField(max_length=254, blank=True, null=True)
    n_heat = models.CharField(max_length=254, blank=True, null=True)
    n_parking = models.CharField(max_length=254, blank=True, null=True)
    n_househol = models.CharField(max_length=254, blank=True, null=True)
    n_area_typ = models.CharField(max_length=254, blank=True, null=True)
    n_security = models.CharField(max_length=254, blank=True, null=True)
    n_other_co = models.CharField(max_length=254, blank=True, null=True)
    n_parking_field = models.CharField(db_column='n_parking_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    n_window_v = models.CharField(max_length=254, blank=True, null=True)
    house_type = models.CharField(max_length=254, blank=True, null=True)
    n_road_som = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'naver_property_final'


class Officetels(models.Model):
    gid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    rent = models.CharField(max_length=254, blank=True, null=True)
    size_cut = models.CharField(max_length=254, blank=True, null=True)
    size = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    deposit = models.BigIntegerField(blank=True, null=True)
    pay = models.BigIntegerField(blank=True, null=True)
    year = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    contract = models.CharField(max_length=254, blank=True, null=True)
    road = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    floor_cut = models.CharField(max_length=254, blank=True, null=True)
    floor = models.BigIntegerField(blank=True, null=True)
    area = models.CharField(max_length=254, blank=True, null=True)
    recent = models.BigIntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    station_ar = models.BigIntegerField(blank=True, null=True)
    station_na = models.CharField(max_length=254, blank=True, null=True)
    transfer = models.BigIntegerField(blank=True, null=True)
    criteria = models.CharField(max_length=254, blank=True, null=True)
    hos_num = models.BigIntegerField(blank=True, null=True)
    mart_num = models.BigIntegerField(blank=True, null=True)
    fast_num = models.BigIntegerField(blank=True, null=True)
    cafe_num = models.BigIntegerField(blank=True, null=True)
    cul_num = models.BigIntegerField(blank=True, null=True)
    con_num = models.BigIntegerField(blank=True, null=True)
    laun_num = models.BigIntegerField(blank=True, null=True)
    da_num = models.BigIntegerField(blank=True, null=True)
    gym_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'officetels'


class OneTwoRoom(models.Model):
    gid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    rent = models.CharField(max_length=254, blank=True, null=True)
    size_cut = models.CharField(max_length=254, blank=True, null=True)
    size = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    deposit = models.BigIntegerField(blank=True, null=True)
    pay = models.BigIntegerField(blank=True, null=True)
    year = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    contract = models.CharField(max_length=254, blank=True, null=True)
    road = models.CharField(max_length=254, blank=True, null=True)
    area = models.CharField(max_length=254, blank=True, null=True)
    recent = models.BigIntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    station_ar = models.BigIntegerField(blank=True, null=True)
    station_na = models.CharField(max_length=254, blank=True, null=True)
    transfer = models.BigIntegerField(blank=True, null=True)
    criteria = models.CharField(max_length=254, blank=True, null=True)
    hos_num = models.BigIntegerField(blank=True, null=True)
    mart_num = models.BigIntegerField(blank=True, null=True)
    fast_num = models.BigIntegerField(blank=True, null=True)
    cafe_num = models.BigIntegerField(blank=True, null=True)
    cul_num = models.BigIntegerField(blank=True, null=True)
    con_num = models.BigIntegerField(blank=True, null=True)
    laun_num = models.BigIntegerField(blank=True, null=True)
    da_num = models.BigIntegerField(blank=True, null=True)
    gym_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'one_two_room'



class Speed(models.Model):
    area = models.CharField(max_length=255, blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speed'


class Villa(models.Model):
    gid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    rent = models.CharField(max_length=254, blank=True, null=True)
    size_cut = models.CharField(max_length=254, blank=True, null=True)
    size = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    deposit = models.BigIntegerField(blank=True, null=True)
    pay = models.BigIntegerField(blank=True, null=True)
    year = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    contract = models.CharField(max_length=254, blank=True, null=True)
    road = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    floor_cut = models.CharField(max_length=254, blank=True, null=True)
    floor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area = models.CharField(max_length=254, blank=True, null=True)
    recent = models.BigIntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    station_ar = models.BigIntegerField(blank=True, null=True)
    station_na = models.CharField(max_length=254, blank=True, null=True)
    transfer = models.BigIntegerField(blank=True, null=True)
    criteria = models.CharField(max_length=254, blank=True, null=True)
    hos_num = models.BigIntegerField(blank=True, null=True)
    mart_num = models.BigIntegerField(blank=True, null=True)
    fast_num = models.BigIntegerField(blank=True, null=True)
    cafe_num = models.BigIntegerField(blank=True, null=True)
    cul_num = models.BigIntegerField(blank=True, null=True)
    con_num = models.BigIntegerField(blank=True, null=True)
    laun_num = models.BigIntegerField(blank=True, null=True)
    da_num = models.BigIntegerField(blank=True, null=True)
    gym_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'villa'

