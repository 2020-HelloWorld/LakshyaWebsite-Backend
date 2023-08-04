from django.db import models
from common.models import company,skills

# Create your models here.

class job(models.Model):
    job_id = models.AutoField(primary_key=True)
    description = models.TextField()
    apply_before = models.DateField()
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    skill = models.ManyToManyField(skills)
    startDate = models.DateField()
    duration = models.CharField(max_length=100)
    ctc = models.CharField(max_length=100)
    aboutCompany = models.TextField()
    aboutInternship = models.TextField()
    whoCanApply = models.TextField()
    postedTime = models.DateTimeField(auto_now_add=True)
    numberofhiring = models.PositiveIntegerField()
    hiringsince = models.DateField()
    numberofopportunities = models.PositiveIntegerField()
    perks = models.TextField()
    numberofopenings = models.PositiveIntegerField()