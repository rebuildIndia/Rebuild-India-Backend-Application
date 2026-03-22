from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    role: str

    class Config:
        from_attributes = True