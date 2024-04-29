from fastapi import APIRouter, HTTPException
from typing import List
from schemas import UserSchema, ShopSchema
from services import UserService, ShopService

user_router = APIRouter(prefix="/users", tags=["users"])
user_service = UserService()

@user_router.get("/", response_model=List[UserSchema])
async def get_users():
    return user_service.get_users()

@user_router.get("/{user_id}", response_model=UserSchema)
async def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

shop_router = APIRouter(prefix="/shops", tags=["shops"])
shop_service = ShopService()

@shop_router.get("/", response_model=List[ShopSchema])
async def get_shops():
    return shop_service.get_shops()

@shop_router.get("/{shop_id}", response_model=ShopSchema)
async def get_shop(shop_id: int):
    shop = shop_service.get_shop(shop_id)
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")
    return shop

