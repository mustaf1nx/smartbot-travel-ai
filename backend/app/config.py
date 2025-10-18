import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DGIS_API_KEY: str = os.getenv("DGIS_API_KEY", "")
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "gemini")
    LLM_API_KEY: str = os.getenv("LLM_API_KEY", "")
    REGION_DEFAULT: str = os.getenv("REGION_DEFAULT", "Алматы")

settings = Settings()
