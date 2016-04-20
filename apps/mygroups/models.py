from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

from apps.groups.models import Groups


class MyGroups(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Groups)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('created_at',)
        app_label = 'my groups'
        db_table = 'app_my_groups'
        verbose_name = 'My Group'
        verbose_name_plural = 'My Groups'
