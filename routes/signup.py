from fastapi import APIRouter, HTTPException
from controllers.signup import signup
from models.user import User
from pydantic import ValidationError

router = APIRouter()

url_prefix = "/api/auth"

@router.post(f"{url_prefix}/signup")
async def signup_route(user: User):
    try:
        return await signup(user)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=f"Validation error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")