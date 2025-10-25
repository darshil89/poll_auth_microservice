from fastapi import FastAPI, Depends
from dotenv import load_dotenv
import os
import uvicorn
from routes.signup import router as signup_router
from routes.signin import router as signin_router
from helpers.db import check_db_connection
load_dotenv()

app = FastAPI()

@app.get("/")
async def read_root():
    db = await check_db_connection()
    if not db:
        return {"message": "Database connection failed"}
    return {"message": "Auth service is running", "database": db}

app.include_router(signup_router)
app.include_router(signin_router)

if __name__ == "__main__":  
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)