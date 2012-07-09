from django.db import models
import datetime

class Region(models.Model):
    state = models.CharField(max_length=25, verbose_name='state name')
    state_abbrev = models.CharField(max_length=2, verbose_name='state')
    county = models.CharField(max_length=25, blank=True)
    imageURL = models.URLField(blank=True)
    def __unicode__(self):
        return u'state:%s (county:%s)' % (self.state_abbrev, county)
    
class Polyline(models.Model):
    region = models.ForeignKey('Region')
    lat = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='latitude')
    lng = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='longitude')
    def __unicode__(self):
        return u'lat:%3.4f lng:%3.4f' % (self.lat, self.lng)

class Category(models.Model):
    name = models.CharField(max_length=25)
    imageURL = models.URLField(blank=True)
    def __unicode__(self):
        return self.name

class Dataset(models.Model):
    category = models.ForeignKey('Category')
    name = models.CharField(max_length=20)
    legend = models.CharField(max_length=25, blank=True)
    description = models.TextField(blank=True)
    imageURL = models.URLField(blank=True)
    citations = models.TextField(blank=True)
    created = models.DateField(editable=False)
    updated = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not 'force_insert' in kwargs:
            kwargs['force_insert'] = False
        if not 'force_update' in kwargs:
            kwargs['force_update'] = False
        if not self.id:
            self.created = datetime.date.today()
        self.updated = datetime.datetime.today()
        super(Patient, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Range(models.Model):
    dataset = models.ForeignKey('Dataset')
    low = models.DecimalField(max_digits=12, decimal_places=3)
    high = models.DecimalField(max_digits=12, decimal_places=3)
    name = models.CharField(max_length=15)
    color = models.CharField(max_length=7)   # eg. #AAA000
    def __unicode__(self):
        return self.name

class Datarow(models.Model):
    dataset = models.ForeignKey('Dataset')
    region = models.ForeignKey('Region')
    value = models.DecimalField(max_digits=12, decimal_places=3)
    def __unicode__(self):
        return self.value

class History(models.Model):
    name = models.CharField(max_length=15)
    searched = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not 'force_insert' in kwargs:
            kwargs['force_insert'] = False
        if not 'force_update' in kwargs:
            kwargs['force_update'] = False
        self.searched = datetime.datetime.today()
        super(Patient, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
    

