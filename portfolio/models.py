from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=300)
    project_description = models.CharField(max_length=300)
    programming_languages = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name} - {self.project_description} - {self.programming_languages}'


class ProgrammingLanguages(models.Model):
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name} '

class Skill(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=350)

    def __str__(self):
        return f'{self.name} - {self.description}'

class Certificate(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=350)
    date = models.DateField()
    company = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name} - {self.description} - {self.date} - {self.company}'