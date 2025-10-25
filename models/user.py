from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from typing import Optional
import re

class User(BaseModel):
    id: Optional[str] = None
    email: str
    name: Optional[str] = None
    password: str
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
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