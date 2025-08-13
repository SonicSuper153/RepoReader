import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
load_dotenv()

class Brain:
    def __inti__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
    
    def getLLM(self, max_token: int = 1000, temperature: float = 0.3) -> GoogleGenerativeAI:
        return GoogleGenerativeAI(
            api_key = self.api_key,
            max_tokens=max_token,
            temperature=temperature,
            model="gemini-2.5-pro"
        )

    def embeddingsModel(self):
        return GoogleGenerativeAIEmbeddings(
            api_key = self.api_key,
            model="models/gemini-embedding-001"
        )
        