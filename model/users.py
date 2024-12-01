from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import String, BigInteger, ForeignKey, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model.database import BaseModel


class UserStatus(PyEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"


class User(BaseModel):
    firstname: Mapped[str] = mapped_column(String(255), nullable=True)
    lastname: Mapped[str] = mapped_column(String(255), nullable=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=True)
    status: Mapped[UserStatus] = mapped_column(Enum(UserStatus), default=UserStatus.ACTIVE, nullable=True)

    freelance: Mapped['Freelance'] = relationship('Freelance', back_populates='user', uselist=False, lazy='selectin')
    business_owner: Mapped['BusinessOwner'] = relationship('BusinessOwner', back_populates='user', uselist=False,
                                                           lazy='selectin')

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email}, status={self.status.name})>"


class Freelance(BaseModel):
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey(User.id, ondelete='CASCADE'), unique=True)
    user: Mapped['User'] = relationship('User', back_populates='freelance', lazy='selectin')

    education: Mapped[list['Education']] = relationship('Education', back_populates='freelance', lazy='selectin')

    def __repr__(self):
        return f"<Freelance(user_id={self.user_id})>"


class BusinessOwner(BaseModel):
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey(User.id, ondelete='CASCADE'), unique=True)
    user: Mapped['User'] = relationship('User', back_populates='business_owner', lazy='selectin')

    def __repr__(self):
        return f"<BusinessOwner(user_id={self.user_id})>"


class Education(BaseModel):
    freelance_id: Mapped[int] = mapped_column(BigInteger, ForeignKey(Freelance.id, ondelete='CASCADE'))
    freelance: Mapped['Freelance'] = relationship('Freelance', back_populates='education', lazy='selectin')

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    started_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    ended_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Education(name={self.name}, freelance_id={self.freelance_id})>"
