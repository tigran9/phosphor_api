from django.contrib.postgres.fields import JSONField
from django.db import models


class Contract(models.Model):
    asset_type = models.CharField(max_length=255)
    asset_model = models.CharField(max_length=255)
    data = JSONField(default=dict)

    def __str__(self):
        return self.asset_type

    class Meta:
        verbose_name_plural = 'Contract'


class Schema(models.Model):
    data = JSONField(default=dict)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Schema'
