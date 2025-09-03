from git import Repo
import os
import shutil
class Helper:
    def clone(self, git_url: str, folder_name: str="cloned_repo") -> str:
        if os.path.exists(folder_name):
            print(f"File {folder_name} already exists")
        else:
            Repo.clone_from(git_url,folder_name)
            print(f"Repo cloned from {folder_name}")
        return folder_name

    def delete(self, folder_path: str):
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path) 
            print(f"{folder_path} has been deleted.")
        else:
            print(f"{folder_path} does not exist.")

    def extractCode(self, folder_name: str="cloned_repo") -> str:
        code_text = ""
        for root, dirs, files in os.walk(folder_name):
            for file in files:
                try:
                    file_path = os.path.join(root,file)
                    test_extension = {
                        # Python & scripts
                        ".py", ".ipynb", ".sh", ".bat", ".ps1",

                        # Web development
                        ".html", ".css", ".scss", ".js", ".jsx", ".ts", ".tsx",

                        # Data & configs
                        ".json", ".yaml", ".yml", ".xml", ".ini", ".toml", ".env",

                        # Documentation
                        ".md", ".txt", ".rst", ".tex",

                        # C / C++ / Java / Go / Rust
                        ".c", ".cpp", ".h", ".hpp", ".java", ".go", ".rs",

                        # Other languages
                        ".php", ".rb", ".swift", ".kt", ".m", ".scala"
                    }
                    _ , ext = os.path.splitext(file)
                    if ext.lower() not in test_extension:
                        continue
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        code_text += f"File {file_path}\n{content}\n\n"
                except Exception as e:
                    print(f"Exception reading file {file} : {e}")
        return code_text

