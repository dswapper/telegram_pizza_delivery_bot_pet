from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

import bot.settings

engine = create_async_engine(bot.settings.DATABASE_URL, future=True, echo=False)

Base = declarative_base()

db_pool = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
