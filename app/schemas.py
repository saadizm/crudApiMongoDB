from pydantic import BaseModel, EmailStr, constr
from datetime import datetime

class UserBaseSchema(BaseModel):
    name: str
    email: str
    role: str
    created_at : datetime
    updated_at : datetime
    
    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    verified: bool = False
    
class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    
class UserResponseSchema(UserBaseSchema):
    id: str

class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema
    
    
    
    