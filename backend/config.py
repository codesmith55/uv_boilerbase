import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///events.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False