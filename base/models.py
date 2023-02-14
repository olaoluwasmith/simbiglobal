from django.db import models

# Create your models here.

class Staff(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    date_of_birth = models.CharField(max_length=50, blank=True)
    designation = models.CharField(max_length=150, blank=True)
    job_title = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    mobile_number = models.CharField(max_length=50, blank=True)
    hometown = models.CharField(max_length=50, blank=True)
    lga = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    place_of_residence = models.CharField(max_length=150, blank=True)
    guarantor = models.CharField(max_length=50, blank=True)
    guarantor_phone = models.CharField(max_length=50, blank=True)
    guarantor_address = models.CharField(max_length=50, blank=True)
    attachment = models.CharField(max_length=50, blank=True)
    appointment_date = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    mobile_number = models.CharField(max_length=50, blank=True)
    place_of_residence = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Utility(models.Model):
    name = models.CharField(max_length=150)
    details = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Utility'
        verbose_name_plural = 'Utilities'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=150)
    details = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
