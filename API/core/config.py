import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    MODEL_ENCODER = os.getenv("Label_Encoder")
    MODEL_PATH = os.getenv("Model")
settings = Config()
