import os
from dotenv import load_dotenv
from brain import Brain
from helper import Helper

load_dotenv() 

class ReadMe:
    def __init__(self):
        self.brain = Brain()
        self.helper = Helper()
    
    def generateReadme(self, github_url: str, generation_method: str = "Standard README"):
        repo_name = github_url.rsplit("/").split("/")[-1]

        local_path = self.helper.clone(github_url,repo_name)
        code_text = self.helper.extractCode(local_path)