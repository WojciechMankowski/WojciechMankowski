from django.shortcuts import render
from .models import Project, ProgrammingLanguages, Skill
from .projectClass import ProjectClass, ProgrammingLanguage
from .updateData import delet_data
# from .connectGithub import save_langues_to_db, saveToDB


def createLangue(langues):
    return ProgrammingLanguage(langues)


def home(request):
    projects = Project.objects.all()
    langues = [project.programming_languages for project in projects]
    langues = [l.split(" ") for l in langues]
    list_projects = []
    for index in range(len(projects)):
        project = ProjectClass(
            name=projects[index].name,
            project_description=projects[index].project_description,
            programming_languages=[createLangue(l) for l in langues[index]]
        )
        list_projects.append(project)
        langues_db = ProgrammingLanguages.objects.all()
    skills = Skill.objects.all()
    return render(request, 'index.html', {'projects': list_projects, 'langues': langues_db, 'skills': skills})


def filter(request, languages):
    projects = Project.objects.raw(f"Select * FROM portfolio_project where programming_languages like '%{languages}%'")
    langues = [project.programming_languages for project in projects]
    langues = [l.split(" ") for l in langues]
    list_projects = []
    for index in range(len(projects)):
        project = ProjectClass(
            name=projects[index].name,
            project_description=projects[index].project_description,
            programming_languages=[createLangue(l) for l in langues[index]]
        )
        list_projects.append(project)
    print(list_projects)
    langues_db = ProgrammingLanguages.objects.all()
    return render(request, 'index.html', {'projects': list_projects, 'langues': langues_db})
