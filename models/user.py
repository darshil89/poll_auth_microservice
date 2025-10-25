from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    name: Optional[str] = None
    password: str
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None