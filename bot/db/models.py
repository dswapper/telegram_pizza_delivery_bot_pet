import datetime

from sqlalchemy import Column, Integer, String, VARCHAR, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from bot.db.base import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)


class User(BaseModel):
    __tablename__ = "users"

    nickname = Column(VARCHAR(255), unique=True)
    fullname = Column(VARCHAR(255), nullable=False)
    telegram_id = Column(Integer, unique=True)
    address = Column(String)
    phone_number = Column(VARCHAR(255))


class TypeOfProducts(BaseModel):
    __tablename__ = 'type_of_products'

    name = Column(VARCHAR(255), nullable=False)


class Product(BaseModel):
    __tablename__ = "products"

    type_id = Column(Integer, ForeignKey('type_of_products.id'), nullable=False, index=True)
    name = Column(VARCHAR(255), nullable=False)
    cost = Column(Integer, nullable=False)
    description = Column(String)


class Ingredient(BaseModel):
    __tablename__ = "ingredients"

    name = Column(VARCHAR(255), nullable=False)


class ProductIngridient(BaseModel):
    __tablename__ = "product_ingredients"

    product_id = Column(Integer, ForeignKey('products.id'), nullable=False, index=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), nullable=False, index=True)


class ProductImage(BaseModel):
    __tablename__ = 'product_images'

    product_id = Column(Integer, ForeignKey('products.id'), nullable=False, index=True)
    image_url = Column(VARCHAR(255), nullable=False)

class Cart(BaseModel):
    __tablename__ = 'carts'

    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False, index=True)
    position_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    size = Column(Integer)
    amount = Column(Integer)

class Order(BaseModel):
    __tablename__ = 'orders'

    ordered_at = Column(DateTime(timezone=True), server_default=func.now())
