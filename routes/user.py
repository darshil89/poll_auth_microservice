from fastapi import APIRouter, HTTPException
from controllers.user import get_user_by_id
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

url_prefix = "/api/auth"

@router.get(f"{url_prefix}/user")
async def get_user_route(user_id: str, token: str):
    try:
        return await get_user_by_id(user_id, token)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
