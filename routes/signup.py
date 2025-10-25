from fastapi import APIRouter
from controllers.signup import signup
from models.user import User

router = APIRouter()

url_prefix = "/api/auth"

@router.post(f"{url_prefix}/signup")
async def signup_route(user: User):
    return await signup(user)