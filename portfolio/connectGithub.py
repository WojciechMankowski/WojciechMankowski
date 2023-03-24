import datetime
from github import Github
from dotenv import load_dotenv
from os import getenv
from portfolio.models import Project, ProgrammingLanguages
from portfolio.projectClass import ProjectClass, ProgrammingLanguage
from collections import defaultdict

load_dotenv()
api_key = getenv('API_KEY')
projects = []


def getRepro(userName: str):
    git = Github(api_key)
    repos = git.get_user(userName)
    print(repos)
    return repos.get_repos()


def createDescrption(repro):
    name = repro.full_name
    git = Github(api_key)
    repro = git.get_repo(name)
    description = repro.description
    if description == None:
        description = ""
    _languages = repro.get_languages()
    languages = [language for language in _languages.keys()]
    languages = " ".join(languages)
    project = ProjectClass(
        name=name[18:], programming_languages=languages, project_description=description)
    return project


def static(repro, date):
    git = Github(api_key)
    repo = git.get_repo(repro)
    commits = repo.get_commits()
    num_commits = 0
    # print(type(commits))
    for commit in commits:
        commit_date = commit.commit.author.date
        # print(type(commit_date))
        if commit_date == date:
            num_commits += 1
    return num_commits


def run():
    data_statics = defaultdict(lambda: 1)
    repros = getRepro("WojciechMankowski")
    date_start = datetime.datetime.now() - datetime.timedelta(days=365)
    today = datetime.datetime.now()
    i = 0
    try:
        for repro in repros:
            while date != today:
                date_start += datetime.timedelta(days=1)
                data_statics[date] += static(repro.full_name, date)
                i = +1
                print(i)
                if i == 180:
                    break
        print(data_statics)
    except StopIteration:
        print('')  # loop end


def saveToDB():
    repros = getRepro("WojciechMankowski")
    for repro in repros:
        obj = createDescrption(repro)

        project = Project(
            name=obj.name, project_description=obj.project_description,
            programming_languages=obj.programming_languages
        )
        project.save()

def save_langues_to_db(languages):
    languages_model = ProgrammingLanguage(languages)
    db_languages = ProgrammingLanguages(name=languages_model.name, slug=languages_model.slug)
    db_languages.save()


if __name__ == '__main__':
    save_langues_to_db()
