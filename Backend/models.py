from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UsersModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int]
    name: Mapped[str]
    email: Mapped[str]
    invate: Mapped[str]
    rang: Mapped[float]
    level: Mapped[int]
