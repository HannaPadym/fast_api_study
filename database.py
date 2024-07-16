from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

db_url: str = f'sqlite+aiosqlite:///task.db'

engine = create_async_engine(db_url)
session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Model(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class TaskOrm(Model):
    name: Mapped[str]
    description: Mapped[str | None] = None


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
