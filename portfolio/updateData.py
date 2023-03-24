from portfolio.models import Project
from portfolio.projectClass import ProjectClass
from .connectGithub import saveToDB
def delet_data():
    Project.objects.all().delete()
    saveToDB()

if __name__ == '__main__':
    delet_data()
