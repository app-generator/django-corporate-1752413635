# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    company = models.CharField(max_length=255, null=True, blank=True)
    b = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Company(models.Model):

    #__Company_FIELDS__
    company.name = models.CharField(max_length=255, null=True, blank=True)
    company.id = models.IntegerField(null=True, blank=True)
    added = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Company_FIELDS__END

    class Meta:
        verbose_name        = _("Company")
        verbose_name_plural = _("Company")


class Vessels(models.Model):

    #__Vessels_FIELDS__
    vessel.id = models.ForeignKey(Company, on_delete=models.CASCADE)
    added = models.DateTimeField(blank=True, null=True, default=timezone.now)
    vessel.name = models.CharField(max_length=255, null=True, blank=True)

    #__Vessels_FIELDS__END

    class Meta:
        verbose_name        = _("Vessels")
        verbose_name_plural = _("Vessels")



#__MODELS__END
