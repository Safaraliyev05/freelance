from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from model.database import BaseModel


class User(BaseModel):
    firstname: Mapped[str] = mapped_column(String(255), nullable=True)
    lastname: Mapped[str] = mapped_column(String(255), nullable=True)
    username: Mapped[str] = mapped_column(String(255), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    phone: Mapped[str] = mapped_column(String(255), unique=True)
    status: Mapped[str] = mapped_column(String(255), unique=True)

    freelance: Mapped[list['Freelance']] = relationship('Freelance', back_populates='user', lazy='selectin')
    business_owner: Mapped[list['BusinessOwner']] = relationship('BusinessOwner', back_populates='user',
                                                                 lazy='selectin')


class Freelance(BaseModel):
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey(User.id, ondelete='CASCADE'))
    user: Mapped['User'] = relationship('User', back_populates='freelance', lazy='selectin')


class BusinessOwner(BaseModel):
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey(User.id, ondelete='CASCADE'))
    user: Mapped['User'] = relationship('User', back_populates='business_owner', lazy='selectin')
