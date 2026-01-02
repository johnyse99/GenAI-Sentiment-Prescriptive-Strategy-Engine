"""
Module: Configuration Manager
Description: Loads environment variables and defines global constants for Project 2.
"""

import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Config:
    # Project Identity
    APP_TITLE = "GenAI Sentiment & Strategy Engine"
    
    # Path Configuration
    # Prioritizes .env value, defaults to data/ folder
    DATA_PATH = os.getenv("DATA_PATH", "data/customer_reviews.csv")
    
    # AI Model Configuration (Placeholder for Project 2 extension)
    # This will be used when you connect a real LLM like OpenAI or WatsonX
    AI_API_KEY = os.getenv("AI_API_KEY", "simulated_key")
    AI_MODEL_NAME = os.getenv("AI_MODEL_NAME", "gpt-3.5-turbo")

# Singleton instance to be used across the project
config = Config()