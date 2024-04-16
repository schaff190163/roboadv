from pydantic import BaseModel
from typing import List, Optional

class StockInfo(BaseModel):
    symbol: str
    last_refreshed: str
    latest_open: float
    latest_high: float
    latest_low: float
    latest_close: float
    latest_adjusted_close: float
    latest_volume: int
    latest_dividend_amount: float
    latest_split_coefficient: float

    class Config:
        orm_mode = True

class Stock(BaseModel):
    symbol: str
    shares: int

    class Config:
        orm_mode = True

class Portfolio(BaseModel):
    id: int
    name: str
    owner_id: int
    stocks: List[Stock] = []

    class Config:
        orm_mode = True

class PortfolioCreate(BaseModel):
    name: str
    owner_id: int

class PortfolioUpdate(BaseModel):
    name: Optional[str] = None
    owner_id: Optional[int] = None

class PortfolioInDB(Portfolio):
    class Config:
        orm_mode = True

class StockInPortfolio(BaseModel):
    portfolio_id: int
    stock_id: int

    class Config:
        orm_mode = True
