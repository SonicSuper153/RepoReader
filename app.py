import os
from dotenv import load_dotenv
from brain import Brain
from helper import Helper
from generators import Generators


load_dotenv() 

class ReadMe:
    def __init__(self):
        self.brain = Brain()
        self.helper = Helper()
        self.generator = Generators()
        self.llm = self.brain.getLLM()
        self.embeddings = self.brain.embeddingsModel()
    
    def generateReadme(self, github_url: str, generation_method: str = "Standard README"):
        repo_name = github_url.rstrip("/").split("/")[-1]

        local_path = self.helper.clone(github_url,repo_name)
        code_text = self.helper.extractCode(local_path)
        summary = self.generator.summarize_code(self.llm,code_text)

        if generation_method == "Standard README":
            readme_content = self.generator.generationRead(self.llm,summary)
        else:
            readme_content = self.generator.generation_from_example_stored_in_vectorDB(self.llm,self.embeddings, summary)
        return readme_content

        