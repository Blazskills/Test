from django.db import models

class Owner(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    profession = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname

class Social_account(models.Model):
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    def __str__(self):
        return self.facebook

class About_me(models.Model):
    breif_introduction = models.CharField(max_length=500)
    date_of_birth = models.CharField(max_length=50)
    breif_introduction = models.CharField(max_length=500)
    language = models.CharField(max_length=50)
    hobbies = models.CharField(max_length=50)
    website = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    def __str__(self):
        return self.hobbies

class Experience(models.Model):
    organization = models.CharField(max_length=500)
    date_of_employment = models.CharField(max_length=500)
    about_organization = models.CharField(max_length=5000)

    def __str__(self):
        return self.organization

class Skills(models.Model):
    Ability = models.CharField(max_length=30)
    def __str__(self):
        return self.Ability

class Percentage(models.Model):
    rate = models.CharField(max_length=3)
    def __str__(self):
        return self.rate
    