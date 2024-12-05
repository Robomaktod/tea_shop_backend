from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    is_deleted: bool

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    password: str


class Tea(BaseModel):
    name: str
    description: str | None = None
    price: float

    class Config:
        orm_mode = True


class Order(BaseModel):
    user_id: int
    tea_id: int
    quantity: int

    class Config:
        orm_mode = True


class Review(BaseModel):
    user_id: int
    tea_id: int
    content: str
    rating: int

    class Config:
        orm_mode = True

class ReviewUpdate(BaseModel):
    content: str
    rating: int

    class Config:
        orm_mode = True