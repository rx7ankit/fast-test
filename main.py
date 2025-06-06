from fastapi import FastAPI
import dotenv
import os

# Load environment variables from .env file
dotenv.load_dotenv()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World! " + os.getenv("KEY", "")}
