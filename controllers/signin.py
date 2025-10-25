from helpers.jwt_auth import create_token_response
from prisma import Prisma
from dotenv import load_dotenv
import bcrypt
from fastapi import HTTPException, status

# Load environment variables
load_dotenv()

async def signin(email: str, password: str):
    print(f"Signin attempt for user: {email}")
    
    prisma = Prisma()
    try:
        # Connect with timeout configuration
        await prisma.connect()
        print("Database connected successfully")
        
        # Find user by email
        user = await prisma.user.find_unique(
            where={"email": email}
        )
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        
        # Verify password
        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        
        # Create and return token response
        return create_token_response(
            user_id=str(user.id),
            email=user.email,
            name=user.name
        )
        
    except HTTPException:
        raise
    except Exception as e:
        error_message = str(e)
        print(f"Database error: {error_message}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {error_message}"
        )
    finally:
        try:
            await prisma.disconnect()
        except:
            pass
