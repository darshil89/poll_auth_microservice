from prisma import Prisma
from fastapi import HTTPException, status
from dotenv import load_dotenv
from helpers.jwt_auth import verify_token
load_dotenv()

async def get_user_by_id(user_id: str, token: str):
    decoded_token = verify_token(token)
    if decoded_token["sub"] != user_id:
        return {"error": "Unauthorized"}
    prisma = Prisma()
    try:
        await prisma.connect()
        user = await prisma.user.find_unique(
            where={"id": user_id}
        )
        return user.model_dump()
    except Exception as e:
        error_message = str(e)
        print(f"Database error: {error_message}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {error_message}"
        )
    finally:
        await prisma.disconnect()