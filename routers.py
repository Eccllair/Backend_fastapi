from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.user_model import User
from database import get_async_session

users_router = APIRouter()

@users_router.get("/")
async def get_users(session: AsyncSession = Depends(get_async_session)):
    return (await session.execute(select(User))).scalars().all()

@users_router.post("/")
async def create_user(session: AsyncSession = Depends(get_async_session)):
    pass

@users_router.put("/{id}")
async def change_user(session: AsyncSession = Depends(get_async_session)):
    pass

@users_router.delete("/{id}")
async def delete_user(session: AsyncSession = Depends(get_async_session)):
    pass