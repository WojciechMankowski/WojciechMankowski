from django.shortcuts import render
from .models import Project
from .projectClass import ProjectClass, ProgrammingLanguage
from .updateData import delet_data
from .connectGithub import saveToDB
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

    return render(request, 'index.html', {'projects': list_projects})


def delet(request):
    delet_data()
    return render(request, 'delet.html')

def update(request,name):
    print(name)
    project = Project.objects.get(name=name)
    return render(request, 'update.html', {'project': project})

