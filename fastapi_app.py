from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from app import ReadMe

app = FastAPI(
    title="Git - AI ReadMe",
    description="ReadMe generator",
    version="2.0.0"
)

try:
    app.mount("/static", StaticFiles(directory="static"), name="static")
except RuntimeError as e:
    print(f"Error while mounting static files: {e}")

templates = Jinja2Templates(directory="templates")

class ReadmeRequest(BaseModel):
    repo_url: str
    generation_method: str = "Standard README"

class ReadmeResponse(BaseModel):
    success: bool
    readme_content: str = ""
    error_message: str = ""
    repo_url: str = ""
    generation_method: str = ""


readmeapp = ReadMe()

@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("home_page.html", {"request": request})

@app.post("/api/generate-readme", response_model=ReadmeResponse)
async def generate_readme(request_data: ReadmeRequest, request: Request):
    try:
        readme_content = readmeapp.generateReadme(
            request_data.repo_url, request_data.generation_method
        )
        return ReadmeResponse(
            success=True,
            readme_content=readme_content,
            repo_url=request_data.repo_url,
            generation_method=request_data.generation_method
        )
    except Exception as e:
        return ReadmeResponse(
            success=False,
            error_message=str(e),
            repo_url=request_data.repo_url,
            generation_method=request_data.generation_method
        )

