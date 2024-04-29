from fastapi import APIRouter
from . import users, shops, products, brands, payments, statistics

router = APIRouter()

router.include_router(users.user_router)
router.include_router(shops.shop_router)