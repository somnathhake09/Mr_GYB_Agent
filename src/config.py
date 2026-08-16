"""
config.py

Central configuration module. This is the ONLY place in the entire
project that should read environment variables directly. Every other
file imports settings from here instead of touching os.environ itself.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Holds all configuration values for the application.
    """

    # --- API Keys ---
    CLAUDE_API_KEY: str = os.getenv("CLAUDE_API_KEY", "")

    # --- Application Settings ---
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "False").lower() == "true"
    MAX_RETRIES: int = int(os.getenv("MAX_RETRIES", "3"))

    # --- Folder Paths ---
    DATA_DIR: str = "data"
    LOGS_DIR: str = "logs"

    @classmethod
    def validate(cls) -> None:
        """
        Check that critical settings are present before the app runs.
        """
        if not cls.CLAUDE_API_KEY:
            raise ValueError(
                "CLAUDE_API_KEY is missing. "
                "Please add it to your .env file."
            )


settings = Config()