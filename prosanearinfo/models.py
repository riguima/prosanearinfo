from typing import Optional
from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from prosanearinfo.database import db


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    password: Mapped[str]
    authenticated: Mapped[Optional[bool]] = mapped_column(default=False)

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return True

    def get_id(self):
        return str(self.id)


class QrCode(Base):
    __tablename__ = 'qrcodes'
    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[str]
    create_at: Mapped[datetime] = mapped_column()


Base.metadata.create_all(db)
