from sqlalchemy import Column, Integer, String, Float, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_deleted = Column(Boolean, default=False)

    orders = relationship("Order", back_populates="user")
    reviews = relationship("Review", back_populates="user")


class Tea(Base):
    __tablename__ = "teas"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)

    orders = relationship("Order", back_populates="tea")
    reviews = relationship("Review", back_populates="tea")


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tea_id = Column(Integer, ForeignKey("teas.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    user = relationship("User", back_populates="orders")
    tea = relationship("Tea", back_populates="orders")


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tea_id = Column(Integer, ForeignKey("teas.id"), nullable=False)
    content = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)

    user = relationship("User", back_populates="reviews")
    tea = relationship("Tea", back_populates="reviews")
