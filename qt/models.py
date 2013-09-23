from django.db import models
from django.contrib.auth.models import User



class Status(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['order']

class Nonconformity(models.Model):
    title = models.CharField(max_length=255)
    status = models.ForeignKey(Status, default=1)
    priority = models.IntegerField(default=0)
    description_short = models.TextField()
    description = models.TextField(null=True, blank=True)
    reproduction = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, related_name='created_tickets')
    assigned = models.ForeignKey(User, related_name='assigned_tickets', null=True, blank=True)
    observers = models.ManyToManyField(User, related_name='observed_tickets', blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    #cost = models.ManyToManyField('Cost', null=True, blank=True)
    problem = models.ForeignKey('Problem', null=True, blank=True)

    def __unicode__(self):
        return self.title

class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    root_cause = models.TextField(null=True, blank=True)
    status = models.ForeignKey('Status')

    def __unicode__(self):
        return self.title

class Action(models.Model):
    problem = models.ForeignKey('Problem')
    actor = models.ForeignKey('Actor')
    target = models.ForeignKey('Target')
    status = models.ForeignKey('Status')
    external_reference = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s - %s' % (self.problem, self.actor)

class Actor(models.Model):
    name = models.CharField(max_length=255)
    email_a = models.EmailField(null=True, blank=True)
    email_cc = models.EmailField(null=True, blank=True)
    email_cci = models.EmailField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class Cost(models.Model):
    nonconformity = models.ForeignKey('Nonconformity')
    category = models.ForeignKey('CostCategory')
    quantity = models.FloatField(default=0)

    def __unicode__(self):
        return self.quantity

class CostCategory(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Target(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey('Status')

    def __unicode__(self):
        return self.name
