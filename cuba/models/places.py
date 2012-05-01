# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from cuba.utils.alias import tran_lazy as _
from cuba.utils import const

import logging
logger = logging.getLogger(__name__)

class Country(models.Model):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_country'
    verbose_name_plural = 'countries'

  name = models.CharField(_('名称'), max_length=const.NAME_LENGTH, help_text=_('国家名称'))

  def __unicode__(self):
    return self.name


class City(models.Model):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_city'
    verbose_name_plural = 'cities'

  name = models.CharField(_('名称'), max_length=const.NAME_LENGTH, help_text=_('城市名称'))
  country = models.ForeignKey(Country)

  def __unicode__(self):
    return self.name