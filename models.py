from django.db import models 

class Division(models.Model):
    name = models.CharField(max_length=15)


class District(models.Model):
    name = models.CharField(max_length=20)
    division = models.ForeignKey(Division)


class SubDistrict(models.Model):
    name = models.CharField(max_length=30)
    district = models.ForeignKey(District)


class Union(models.Model):
    name = models.CharField(max_length=50)
    sub_district = models.ForeignKey(SubDistrict)
