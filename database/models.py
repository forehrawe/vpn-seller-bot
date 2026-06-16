from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Text
from .config import engine, Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, unique=True)
    is_admin = Column(Boolean, default=False)
    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("users.account_id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    completed = Column(Boolean, default=False)
    
    user = relationship("User", back_populates="orders")
    
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    region = Column(String)
    volume = Column(Integer)
    price = Column(Integer)
    
class Ticket(Base):
    __tablename__ = "tickets"
    
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("users.account_id"))
    title = Column(String)
    problem = Column(Text)
    problematic_order = Column(Integer, ForeignKey("orders.id"))
    
    
Base.metadata.create_all(bind=engine)

