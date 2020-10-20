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