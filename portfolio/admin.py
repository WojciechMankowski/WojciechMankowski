from django.contrib import admin
from .models import Project, ProgrammingLanguages, Skill, Certificate

# Register your models here.
admin.site.register(Project)
admin.site.register(ProgrammingLanguages)
admin.site.register(Skill)
admin.site.register(Certificate)

