"""
Configuration Management
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration."""

    # LinkedIn
    LINKEDIN_ACCESS_TOKEN = os.getenv('LINKEDIN_ACCESS_TOKEN')
    LINKEDIN_ORG_ID = os.getenv('LINKEDIN_ORG_ID')

    # Twitter
    TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
    TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

    # OpenAI
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    # App
    APP_ENV = os.getenv('APP_ENV', 'development')
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    TIMEZONE = os.getenv('TIMEZONE', 'UTC')
