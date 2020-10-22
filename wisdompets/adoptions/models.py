from django.db import models

# Create your models here.
class Pet(models.Model):
    #[('value_that_stores_in_database'),('string_that_will_be_displayed_inf_form_&_django-admin')]
    SEX_CHOICES = [('M', 'Male'), ('F','Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

    def __str__(self):
        return self.name

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


    