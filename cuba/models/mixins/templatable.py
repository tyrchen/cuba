# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from cuba.utils import const
from cuba.utils.alias import tran_lazy as _
import logging
logger = logging.getLogger(__name__)

class TemplatePathNotConfigured(Exception):
  pass

class Templatable(models.Model):
  """
  Abstract model that provides templating capability an object for a user.
  """

  class Meta:
    abstract = True

  template_name = models.CharField(_('模板名称'), max_length=const.NAME_LENGTH,
                                   help_text=_(''),
                                   blank=True, default='')
  template_info = models.TextField(_('XML格式的模板参数'), help_text=_(''), blank=True, default='')

  def get_template_info(self):
    from cuba.vendors import xmltodict
    if self.template_info:
      try:
        template_info = xmltodict.parse(self.template_info)['info']
      except Exception:
        template_info = {}
    else:
      template_info = {}
    return template_info