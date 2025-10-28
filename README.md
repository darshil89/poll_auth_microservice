# Auth Microservice

A secure authentication microservice built with FastAPI, Prisma, and MongoDB. This service handles user registration, authentication, and JWT token management for the QuickPoll platform.

## 🚀 Features

- **User Registration**: Secure user signup with email validation
- **User Authentication**: Login with email/password authentication
- **JWT Token Management**: Secure token generation and validation
- **Password Security**: Bcrypt hashing for password protection
- **Database Integration**: MongoDB with Prisma ORM
- **CORS Support**: Cross-origin resource sharing enabled
- **Input Validation**: Pydantic models for request validation
- **Error Handling**: Comprehensive error handling and logging

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.8+
- **Database**: MongoDB
- **ORM**: Prisma Client Python
- **Authentication**: JWT (PyJWT)
- **Password Hashing**: Bcrypt
- **Validation**: Pydantic
- **Server**: Uvicorn
- **Environment**: Python-dotenv

## 📁 Project Structure

```
auth_microservice/
├── controllers/                      # Business logic controllers
│   ├── __init__.py                  # Package initialization
│   ├── signin.py                    # User signin logic
│   ├── signup.py                    # User signup logic
│   └── user.py                      # User management logic
├── helpers/                         # Utility and helper functions
│   ├── auth_middleware.py           # Authentication middleware
│   ├── db.py                        # Database connection utilities
│   └── jwt_auth.py                  # JWT token management
├── models/                          # Pydantic data models
│   └── user.py                      # User model with validation
├── routes/                          # FastAPI route definitions
│   ├── __init__.py                  # Package initialization
│   ├── signin.py                    # Signin API routes
│   ├── signup.py                    # Signup API routes
│   └── user.py                      # User API routes
├── main.py                          # FastAPI application entry point
├── requirements.txt                 # Python dependencies
└── schema.prisma                    # Prisma database schema
```

## 🚦 Getting Started

### Prerequisites

- Python 3.8 or higher
- MongoDB instance running
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd auth_microservice
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**
   
   Create a `.env` file in the root directory:
   ```env
   AUTH_DATABASE_URL="mongodb://localhost:27017/quickpoll_auth"
   JWT_SECRET_KEY="your-super-secret-jwt-key-here"
   ```

5. **Generate Prisma Client**
   ```bash
   prisma generate
   ```

6. **Start the development server**
   ```bash
   python main.py
   ```

7. **Verify the service**
   
   The service will be available at `http://localhost:8000`
   
   Check the health endpoint: `GET http://localhost:8000/`

## 📜 API Endpoints

### Authentication Routes

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| `POST` | `/api/auth/signup` | Register a new user | `User` object |
| `POST` | `/api/auth/signin` | Authenticate user | `SignInRequest` object |
| `GET` | `/api/auth/user` | Get user by ID | Query params: `user_id`, `token` |

### Request/Response Examples

#### User Registration
```http
POST /api/auth/signup
Content-Type: application/json

{
  "email": "user@example.com",
  "name": "John Doe",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 1800,
  "user": {
    "id": "user_id_here",
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

#### User Login
```http
POST /api/auth/signin
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 1800,
  "user": {
    "id": "user_id_here",
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

## 🏗️ Architecture Overview

### Authentication Flow

1. **Registration**: User provides email, name, and password
2. **Validation**: Input validation using Pydantic models
3. **Password Hashing**: Bcrypt hashing before database storage
4. **User Creation**: User stored in MongoDB via Prisma
5. **Token Generation**: JWT token created and returned

### Database Schema

The service uses MongoDB with the following user model:

```prisma
model User {
    id        String   @id @default(auto()) @map("_id") @db.ObjectId
    email     String   @unique
    name      String?
    password  String
    createdAt DateTime @default(now())
    updatedAt DateTime @updatedAt
}
```

### Security Features

- **Password Hashing**: Bcrypt with salt for secure password storage
- **JWT Tokens**: Secure token-based authentication
- **Input Validation**: Email format and password strength validation
- **CORS Protection**: Configurable cross-origin resource sharing
- **Error Handling**: Secure error messages without sensitive data exposure

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `AUTH_DATABASE_URL` | MongoDB connection string | Yes | - |
| `JWT_SECRET_KEY` | Secret key for JWT signing | Yes | - |

### JWT Configuration

- **Algorithm**: HS256
- **Token Expiry**: 30 minutes
- **Token Type**: Bearer

### CORS Configuration

The service is configured to allow:
- All origins (`*`)
- All methods (`*`)
- All headers (`*`)
- Credentials enabled

## 🚀 Deployment

### Production Build

1. **Install production dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables**
   ```bash
   export AUTH_DATABASE_URL="your-production-mongodb-url"
   export JWT_SECRET_KEY="your-production-secret-key"
   ```

3. **Generate Prisma Client**
   ```bash
   prisma generate
   ```

4. **Run with Uvicorn**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN prisma generate

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🧪 Development

### Code Structure Guidelines

- **Controllers**: Business logic and database operations
- **Routes**: API endpoint definitions and request handling
- **Models**: Pydantic models for data validation
- **Helpers**: Utility functions and shared logic

### Adding New Features

1. **Create Models**: Define Pydantic models in `models/`
2. **Add Controllers**: Implement business logic in `controllers/`
3. **Define Routes**: Create API endpoints in `routes/`
4. **Update Main**: Register new routers in `main.py`

### Database Operations

The service uses Prisma Client for database operations:

```python
from prisma import Prisma

prisma = Prisma()
await prisma.connect()

# Database operations
user = await prisma.user.find_unique(where={"email": email})

await prisma.disconnect()
```

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Verify MongoDB is running
   - Check `AUTH_DATABASE_URL` environment variable
   - Ensure network connectivity

2. **JWT Secret Key Error**
   - Set `JWT_SECRET_KEY` environment variable
   - Use a strong, random secret key

3. **Prisma Client Not Generated**
   - Run `prisma generate` after installing dependencies
   - Check Prisma schema syntax

4. **Import Errors**
   - Ensure virtual environment is activated
   - Verify all dependencies are installed

### Debug Mode

Enable debug logging by setting the log level in your environment:

```bash
export LOG_LEVEL=DEBUG
```

## 📝 API Documentation

Once the service is running, you can access:

- **Interactive API Docs**: `http://localhost:8000/docs`
- **ReDoc Documentation**: `http://localhost:8000/redoc`
- **OpenAPI Schema**: `http://localhost:8000/openapi.json`

## 🔒 Security Considerations

- **JWT Secret**: Use a strong, randomly generated secret key
- **Password Policy**: Enforce strong password requirements
- **HTTPS**: Use HTTPS in production environments
- **Rate Limiting**: Consider implementing rate limiting for auth endpoints
- **Token Expiry**: Configure appropriate token expiration times

## 📊 Monitoring

### Health Check

Monitor service health using the root endpoint:

```bash
curl http://localhost:8000/
```

### Database Health

The service includes database connection checking:

```python
# Check database connection
db_status = await check_db_connection()
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is part of the QuickPoll microservices architecture.

---

**Auth Microservice** - Built with ❤️ using FastAPI and Python
