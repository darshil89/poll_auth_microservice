from fastapi import APIRouter, HTTPException
from controllers.signin import signin
from pydantic import BaseModel, EmailStr, validator
from pydantic import ValidationError
import re

router = APIRouter()

url_prefix = "/api/auth"

class SignInRequest(BaseModel):
    email: str
    password: str
    
    @validator('email')
    def validate_email(cls, v):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', v):
            raise ValueError('Invalid email format')
        return v
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        return v

@router.post(f"{url_prefix}/signin")
async def signin_route(credentials: SignInRequest):
    try:
        return await signin(credentials.email, credentials.password)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=f"Validation error: {e}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
