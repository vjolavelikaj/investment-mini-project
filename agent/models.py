from django.db import models

INVESTOR_TYPES = (
    (1, 'Person'),
    (2, 'Institution')
)


class Bank(models.Model):
    name = models.CharField(max_length=100, blank=False, default='', null=False)
    location = models.CharField(max_length=500, null=True)
    contact = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Investor(models.Model):
    name = models.CharField(max_length=100, blank=False, default='', null=False)
    type = models.IntegerField(choices=INVESTOR_TYPES, null=False)
    location = models.CharField(max_length=500, null=True)
    contact = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
