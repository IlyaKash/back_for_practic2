from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    username: str
    email: str

class Store(BaseModel):
    id: int
    name: str
    location: str

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str]

class Brand(BaseModel):
    id: int
    name: str
    country: str

class Payment(BaseModel):
    id: int
    amount: float
    status: str

class Statistic(BaseModel):
    id: int
    value: float
