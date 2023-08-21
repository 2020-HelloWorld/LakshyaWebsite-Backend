from django.contrib import admin
from .models import *


# Register the models in the admin interface
admin.site.register(Internship)
admin.site.register(internshipApplied)

