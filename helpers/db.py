# Checking if the database is connected
from prisma import Prisma

async def check_db_connection():
    prisma = Prisma()
    try:
        await prisma.connect()
        await prisma.disconnect()
        return True
    except Exception as e:
        print(f"Error checking database connection: {e}")
        return False