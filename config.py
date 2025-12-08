"""
Configuration Module
Contains application configuration settings for different environments
"""

import os

class Config:
    """Base configuration class"""

    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    # Admin password hash (SHA-256). In production set ADMIN_PASSWORD_HASH env var.
    ADMIN_PASSWORD_HASH = os.environ.get('ADMIN_PASSWORD_HASH') or '0e8f52c4edbc35751a23dc00ff1639781bbf5d191129899c7f27e84af59d371c'

    # Database settings
    DATABASE_NAME = 'users.db'

    # Server settings
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = False

class DevelopmentConfig(Config):
    """Development environment configuration"""
    DEBUG = True
    DATABASE_NAME = 'users_dev.db'

class ProductionConfig(Config):
    """Production environment configuration"""
    DEBUG = False
    # In production, always use environment variables for sensitive data
    SECRET_KEY = os.environ.get('SECRET_KEY')

class TestingConfig(Config):
    """Testing environment configuration"""
    TESTING = True
    DATABASE_NAME = 'users_test.db'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
