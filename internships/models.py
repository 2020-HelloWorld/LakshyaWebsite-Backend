# from django.db import models
# from common.models import company,skills

# # Create your models here.

# class internship(models.Model):
#     internship_id = models.AutoField(primary_key=True)
#     description = models.TextField()
#     apply_before = models.DateField()
#     company = models.ForeignKey(company, on_delete=models.CASCADE)
#     skill = models.ManyToManyField(skills)
#     startDate = models.DateField()
#     duration = models.CharField(max_length=100)
#     stipend = models.CharField(max_length=100)
#     aboutCompany = models.TextField()
#     aboutInternship = models.TextField()
#     whoCanApply = models.TextField()
#     postedTime = models.DateTimeField(auto_now_add=True)
#     numberofhiring = models.PositiveIntegerField()
#     hiringsince = models.DateField()
#     numberofopportunities = models.PositiveIntegerField()
#     perks = models.TextField()
#     numberofopenings = models.PositiveIntegerField()

from django.db import models
from django.core.validators import MinValueValidator
from common.models import company, skills

# class Internships(models.Model):
#     company1 = models.ForeignKey(company, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     duration = models.PositiveIntegerField(validators=[MinValueValidator(1)])
#     stipend = models.DecimalField(max_digits=10, decimal_places=2)
#     about_job = models.TextField()
#     skills_required = models.ManyToManyField('skills')
#     who_can_apply = models.CharField(max_length=500)
#     posted_time = models.DateTimeField(auto_now_add=True)
#     number_of_hiring = models.PositiveIntegerField(default=1)
#     hiring_since = models.DateField()
#     number_of_opportunities = models.PositiveIntegerField(default=1)
#     perks = models.CharField(max_length=500)
#     number_of_openings = models.PositiveIntegerField(default=1)


class internship:
    skill_id = models.ForeignKey(skills, on_delete=models.CASCADE)