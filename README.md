# RepoReader

**Built with:** Python, FastAPI, LangChain, Google Generative AI  

---

## Description
**RepoReader** is an AI-powered tool that automatically generates a high-quality `README.md` for any GitHub repository. By analyzing the codebase, extracting key components, and summarizing functionality, it produces clear and structured documentation that can save developers hours of manual writing.  

It leverages **LangChain** for code summarization and **Google Generative AI** for text generation, offering both standard README generation and advanced example-driven generation using vector stores.

---

## Features
- Automatic codebase analysis and summarization.
- Generates structured README files including architecture, installation, usage, and API references.
- Supports advanced generation using vector stores to incorporate real-world example templates.
- Web interface built with FastAPI for easy usage.
- Handles large repositories with intelligent chunking and summarization.

---

## Architecture
**Components:**
1. **Helper:** Clones repositories and extracts code.
2. **Generators:** Summarizes code and generates README content.
3. **Brain:** Connects to Google Generative AI models for LLM and embeddings.
4. **FastAPI App:** Provides REST API endpoints and a web interface for generating README files.

---

## Prerequisites
- Python 3.10+
- Git
- Google API Key (set in `.env` file)
- Dependencies: Listed in `requirements.txt`

---

## Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/SonicSuper153/RepoReader.git
   cd RepoReader
   
2. Activate the Virtual Environment

Linux / macOS

source venv/bin/activate


Windows

venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Set Up Environment Variables

Create a .env file in the project root and add your Google API key:

GOOGLE_API_KEY=your_google_api_key_here
