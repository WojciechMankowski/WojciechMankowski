from dataclasses import dataclass
from typing import List

@dataclass
class ProgrammingLanguage:
    name: str
    slug: str

    def __init__(self, name: str):
        self.name = name
        self.slug = self.creaeSlug()
    def creaeSlug(self):
        return self.name.lower()
@dataclass
class ProjectClass:
    name: str
    programming_languages: str
    project_description: str 

