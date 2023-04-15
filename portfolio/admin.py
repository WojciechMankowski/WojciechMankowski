from django.contrib import admin
from .models import Project, ProgrammingLanguages, Skill, Certificate
class ProgrammingLanguagesAdmin(admin.ModelAdmin):
    search_fields = ['name']

    # admin.ModelAdmin):
    # ...
    # search_fields = ('title', 'body')
# Register your models here.
admin.site.register(Project)
admin.site.register(ProgrammingLanguages, ProgrammingLanguagesAdmin)
admin.site.register(Skill)
admin.site.register(Certificate)

