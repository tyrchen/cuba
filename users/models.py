from __future__ import unicode_literals

from django.db import models
from core import const
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.OneToOneField(User)
  addr = models.CharField(_('个人的唯一URL'), max_length=const.NAME_LENGTH, help_text=_(''))
  bio  = models.CharField(_('个人简介'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''))
  languages = models.CharField(_('语言'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''))
  
