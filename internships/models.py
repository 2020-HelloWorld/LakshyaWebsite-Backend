import datetime
from django.db import models
from django.core.validators import MinValueValidator
from common.models import company, candidate

# class Company(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Skill(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Internship(models.Model):
#     internship_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     apply_before = models.DateField()
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     skills_required = models.ManyToManyField(Skill, through='InternshipSkill')
#     duration = models.CharField(max_length=50)
#     stipend = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.internship_id}: {self.title}"


# class InternshipSkill(models.Model):
#     internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
#     skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.internship} requires {self.skill}"





class Internship(models.Model):
    internship_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25,null=True)
    location = models.CharField(max_length=20,default="Remote")
    description = models.TextField()
    apply_before = models.DateField(null=True)
    stipend = models.FloatField(null=True)
    type = models.CharField(max_length=10,null= True)
    skills = models.CharField(max_length=500,null=True)
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    startdate = models.DateField(null=True)
    duration=models.CharField(max_length=50,null=True)
    aboutCompany = models.CharField(max_length=500,null=True)
    whoCanApply = models.CharField(max_length=150,null=True)
    postedTime = models.TimeField(null=True)
    openings = models.IntegerField(null=True)
    perks = models.CharField(max_length=500,null=True)
    numberofhiring = models.FloatField(null=True)
    numberofopportunities = models.FloatField(null=True)


        
class internshipApplied(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('internship','candidate'))