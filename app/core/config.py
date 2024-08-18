import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    JOBS_DB_URL: str = os.getenv("JOBS_DB_URL", "sqlite:///./app/db/jobs.sqlite")


settings = Settings()