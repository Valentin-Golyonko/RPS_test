from random import randint

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session


class DBConf:
    DATABASE_URL = "postgresql+psycopg://postgres:postgres@127.0.0.1:5432/rps_test"
    engine = create_engine(
        url=DATABASE_URL,
        echo=False,
        pool_size=1_000,
        max_overflow=5_000,
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Dependency to get the database session"""
    database = DBConf.SessionLocal()
    try:
        yield database
    finally:
        database.close()


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
def sync_user_foo(db: Session = Depends(get_db)):
    return db.query(CustomUser).filter(CustomUser.id == randint(1, 1_000_001)).first()


@app.get("/fa_async_user_foo", response_model=UserSch)
async def async_user_foo(db: Session = Depends(get_db)):
    return db.query(CustomUser).filter(CustomUser.id == randint(1, 1_000_001)).first()
