from random import randint

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import String, create_engine, select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

sync_engine = create_engine(
    url="postgresql+psycopg://postgres:postgres@127.0.0.1:5432/rps_test",
    echo=False,
    pool_size=1_000,
    max_overflow=5_000,
)
SyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)

async_engine = create_async_engine(
    # url="postgresql+psycopg://postgres:postgres@127.0.0.1:5432/rps_test",
    url="postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/rps_test",
    echo=False,
    pool_size=1_000,
    max_overflow=5_000,
)
AsyncSessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine
)


class Base(DeclarativeBase):
    pass


class CustomUser(Base):
    __tablename__ = "dj_core_customuser"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(150))


class UserSch(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


app = FastAPI()


@app.get("/fa_sync_dummy_foo")
def sync_dummy_foo():
    return {"message": "fa_sync_dummy_foo"}


@app.get("/fa_async_dummy_foo")
async def async_dummy_foo():
    return {"message": "fa_async_dummy_foo"}


@app.get("/fa_sync_user_foo", response_model=UserSch)
def sync_user_foo():
    with SyncSessionLocal() as session:
        user = (
            session.query(CustomUser)
            .filter(CustomUser.id == randint(1, 1_000_001))
            .first()
        )
    return user


@app.get("/fa_async_user_foo", response_model=UserSch)
async def async_user_foo():
    async with AsyncSessionLocal() as session:
        stmt = select(CustomUser).filter(CustomUser.id == randint(1, 1_000_001))
        results = await session.execute(stmt)
        user = results.scalars().first()
    return user
