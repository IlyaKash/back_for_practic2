from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Импорт контроллеров
from controllers import users, stores, products, brands, payments, statistics

app = FastAPI()

# Подключение CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутов для контроллеров
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(stores.router, prefix="/stores", tags=["stores"])
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(brands.router, prefix="/brands", tags=["brands"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(statistics.router, prefix="/statistics", tags=["statistics"])
