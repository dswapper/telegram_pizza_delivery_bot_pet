from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from bot.db.models import *


async def register_user(session: AsyncSession, user: User):
    session.add(user)
    await session.commit()


async def is_registered(telegram_id, session: AsyncSession):
    req_telegram_id = select(User).where(User.telegram_id == telegram_id)
    response = await session.execute(req_telegram_id)
    return len(list(response)) > 0
