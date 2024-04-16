from pydantic import BaseModel
from typing import List

class PortfolioBase(BaseModel):
    name: str

class PortfolioCreate(PortfolioBase):
    pass

class Portfolio(PortfolioBase):
    id: int
    stocks: List["Stock"] = []

    class Config:
        orm_mode = True

class Stock(BaseModel):
    symbol: str
    shares: int

class StockData(BaseModel):
    symbol: str
    company_name: str
    latest_price: float
    change: float
    change_percent: float
