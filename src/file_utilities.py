# src/utilities.py
import os
from dotenv import load_dotenv, find_dotenv

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

def get_project_root():
    dotenv_path = find_dotenv()
    return os.path.split(dotenv_path)[0]
