import os
from dotenv import load_dotenv

load_dotenv()

# By running `setup_environment.py` you will have the required env variables configured 
# and can now run any of the in-class examples

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")