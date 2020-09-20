from django.contrib import admin

# Register your models here.
from vacancy.models import Candidate, Job, Company, Location, Offer, Salary, Contact

admin.site.register(Job)
admin.site.register(Candidate)
admin.site.register(Company)
admin.site.register(Location)
admin.site.register(Offer)
admin.site.register(Salary)
admin.site.register(Contact)
