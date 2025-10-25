from models.user import User
from helpers.db import check_db_connection
from prisma.client import Prisma

async def signup(user: User):
    try:
        if not await check_db_connection():
            raise Exception("Database connection failed")
        
        prisma = Prisma()
        await prisma.connect()
        created_user = await prisma.user.create(
            data={
                "email": user.email,
                "name": user.name,
                "password": user.password,
            }
        )
        await prisma.disconnect()
        return {
            "message": "User created successfully",
            "user": created_user
        }
    except Exception as e:
        print(f"Error signing up user: {e}")
        return {"error": str(e)}
    finally:
        await prisma.disconnect()