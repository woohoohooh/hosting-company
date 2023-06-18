from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=300)

class Client(models.Model):
    login = models.CharField(max_length=300, null=True)
    email = models.EmailField(max_length=300, null=True)
    name = models.CharField(max_length=300, null=True)
    telegram = models.CharField(max_length=300, null=True)
    phone = models.CharField(max_length=300, null=True)
    data_register = models.DateTimeField(auto_now_add=True, null=True)
    balance = models.IntegerField(null=True)
    password = models.CharField(max_length=300)
    service = models.ManyToManyField(Service)

    # plan = models.ManyToManyField(models.Plans)
    # period = models.ManyToManyField()

    # notifications = models.ForeignKey()
    # access_history = models.ForeignKey()
    # ip_access = models.ForeignKey()
    # networks_access = models.ForeignKey()
    # two_factor_access = models.ForeignKey()
    # trusted_additional = models.CharField(max_length=300)
    # payers_additional = models.CharField(max_length=300)
    # partnership = models.CharField(max_length=300)
    # tickets = models.CharField(max_length=300)
    # offer_ideas = models.CharField(max_length=300)
    # timezone = models.DateField()

# class Services(models.Model):
#     period = models.ManyToManyField(models.Period)
#     plan = models.ManyToManyField(models.Plans)
#     service = models.CharField(max_length=300)
#
# class Plans(models.Model):
#     period = models.ManyToManyField(models.Period)
#     service = models.ManyToManyField(models.Services)
#     plan = models.CharField(max_length=300)
#
# class Period(models.Model):
#     plan = models.ManyToManyField(models.Plans)
#     service = models.ManyToManyField(models.Services)
#     period = models.CharField(max_length=300)

