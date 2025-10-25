from fastapi import FastAPI
from dotenv import load_dotenv
import os
import uvicorn
from routes.signup import router as signup_router
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Auth service is running"}

app.include_router(signup_router)

if __name__ == "__main__":  
    uvicorn.run(app, host="0.0.0.0", port=8000)