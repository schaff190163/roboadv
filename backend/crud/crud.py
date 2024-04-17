from sqlalchemy.orm import Session
from crud.models import Portfolio, Stock
from api.api_types import PortfolioCreate, PortfolioUpdate, StockCreate

class CRUD:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_portfolio(self, portfolio_data: PortfolioCreate, owner_id: int):
        portfolio = Portfolio(**portfolio_data.dict(), owner_id=owner_id)
        self.db_session.add(portfolio)
        self.db_session.commit()
        self.db_session.refresh(portfolio)
        return portfolio

    def get_portfolio(self, portfolio_id: int):
        return self.db_session.query(Portfolio).filter(Portfolio.id == portfolio_id).first()

    def update_portfolio(self, portfolio_id: int, portfolio_data: PortfolioUpdate):
        portfolio = self.get_portfolio(portfolio_id)
        for key, value in portfolio_data.dict().items():
            setattr(portfolio, key, value)
        self.db_session.commit()
        return portfolio

    def delete_portfolio(self, portfolio_id: int):
        portfolio = self.get_portfolio(portfolio_id)
        self.db_session.delete(portfolio)
        self.db_session.commit()

    def add_stock_to_portfolio(self, portfolio_id: int, stock_data: StockCreate):
        stock = Stock(**stock_data.dict(), portfolio_id=portfolio_id)
        self.db_session.add(stock)
        self.db_session.commit()
        self.db_session.refresh(stock)
        return stock

    def remove_stock_from_portfolio(self, portfolio_id: int, stock_id: int):
        stock = self.db_session.query(Stock).filter(Stock.portfolio_id == portfolio_id, Stock.id == stock_id).first()
        self.db_session.delete(stock)
        self.db_session.commit()
