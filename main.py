from openai import OpenAI 
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
  organization=os.getenv("OPENAI_ORGANIZATION"),
  project=os.getenv("OPENAI_PROJECT"),
  api_key=os.getenv("OPENAI_APIKEY")
)

