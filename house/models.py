from django.db import models

class Officetels(models.Model):
    gid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    rent = models.CharField(max_length=254, blank=True, null=True)
    size = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    deposit = models.BigIntegerField(blank=True, null=True)
    pay = models.BigIntegerField(blank=True, null=True)
    year = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    contract = models.CharField(max_length=254, blank=True, null=True)
    road = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
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
        # managed = False
        db_table = 'officetels'


class OneTwoRoom(models.Model):
    gid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    rent = models.CharField(max_length=254, blank=True, null=True)
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
        # managed = False
        db_table = 'one_two_room'


class Villa(models.Model):
    gid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    rent = models.CharField(max_length=254, blank=True, null=True)
    size = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    deposit = models.BigIntegerField(blank=True, null=True)
    pay = models.BigIntegerField(blank=True, null=True)
    year = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    contract = models.CharField(max_length=254, blank=True, null=True)
    road = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
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
        # managed = False
        db_table = 'villa'


class Speed(models.Model):
    area = models.CharField(max_length=255, blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'speed'