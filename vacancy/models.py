import uuid

from django.db import models


# Create your models here.

class Job(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    premium = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    company = models.ForeignKey(
        "vacancy.Company", on_delete=models.PROTECT,
        related_name="Job_to_company")
    candidate = models.ForeignKey(
        "vacancy.Candidate", on_delete=models.PROTECT,
        related_name="job_to_candidate")
    offer = models.ForeignKey(
        "vacancy.Offer", on_delete=models.PROTECT,
        related_name="job_to_offer")
    contact = models.ForeignKey(
        "vacancy.Contact", on_delete=models.PROTECT,
        related_name="job_to_contact")


class Candidate(models.Model):
    level = models.CharField(max_length=64)
    skill = models.CharField(max_length=64)
    stack = models.CharField(max_length=256)


class Company(models.Model):
    name = models.CharField(max_length=64)
    industry = models.CharField(max_length=64)
    website = models.CharField(max_length=64)
    location = models.ForeignKey(
        "vacancy.Location", on_delete=models.PROTECT,
        related_name="company_to_location")
    remote = models.BooleanField()


class Location(models.Model):
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)


class Offer(models.Model):
    salary = models.ForeignKey(
        "vacancy.Salary", on_delete=models.PROTECT,
        related_name="Offer_to_salary")
    description = models.CharField(max_length=4096, null=True, blank=True)


class Salary(models.Model):
    From = models.IntegerField()
    to = models.IntegerField()


class Contact(models.Model):
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    telegram = models.CharField(max_length=64)
