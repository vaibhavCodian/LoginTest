from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    type = Column(String, nullable=False, default='admin')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Purchases(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True, nullable=False)
    ProductName = Column(String, nullable=False)
    Price = Column(String, nullable=False)
    purchased_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("customers.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("Customers")


class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, nullable=False)
    Name = Column(String, nullable=False)
    Age = Column(Integer, nullable=False)
    Gender = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))