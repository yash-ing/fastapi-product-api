from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    inventory: int
    description: str | None = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    model_config = {"from_attributes": True}  # pydantic v2 - allow reading from ORM
