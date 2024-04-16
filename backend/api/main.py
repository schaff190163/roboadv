from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from api.api_types import Portfolio, Stock, StockData

import api.api_types as ApiTypes

resources = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Start the character device reader"""
    print('Lifespan started')
    engine = create_engine('sqlite:///database.db')
    resources['crud'] = Crud(engine)
    yield
    engine.dispose()
    resources.clear()
    print('Lifespan finished')


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost",
    "http://localhost:5001",
    "http://localhost:5001/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/portfolios', response_model=List[Portfolio])
async def read_portfolios():
    portfolios = resources['crud'].get_all_portfolios()
    return portfolios


@app.get('/portfolios/{portfolio_id}', response_model=Portfolio)
async def read_portfolio(portfolio_id: int):
    portfolio = resources['crud'].get_portfolio(portfolio_id)
    if portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return portfolio


@app.post('/portfolios', response_model=Portfolio)
async def create_portfolio(portfolio: Portfolio):
    return resources['crud'].create_portfolio(portfolio)


@app.put('/portfolios/{portfolio_id}', response_model=Portfolio)
async def update_portfolio(portfolio_id: int, portfolio: Portfolio):
    return resources['crud'].update_portfolio(portfolio_id, portfolio)


@app.delete('/portfolios/{portfolio_id}')
async def delete_portfolio(portfolio_id: int):
    return resources['crud'].delete_portfolio(portfolio_id)


@app.post('/portfolios/{portfolio_id}/stocks', response_model=Stock)
async def add_stock(portfolio_id: int, stock: Stock):
    return resources['crud'].add_stock_to_portfolio(portfolio_id, stock)


@app.delete('/portfolios/{portfolio_id}/stocks/{stock_id}')
async def remove_stock(portfolio_id: int, stock_id: int):
    return resources['crud'].remove_stock_from_portfolio(portfolio_id, stock_id)


def get_stock_data(symbol: str) -> dict:
    api_key = 'TTMLZZ1KCRAI3MXF'
    endpoint = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    
    try:
        response = requests.get(endpoint)
        data = response.json()
        
        if "Global Quote" not in data:
            raise HTTPException(status_code=404, detail="Stock data not found")

        stock_data = data["Global Quote"]

        stock_info = {
            "symbol": stock_data["01. symbol"],
            "company_name": "Company Name",
            "latest_price": float(stock_data["05. price"]),
            "change": float(stock_data["09. change"]),
            "change_percent": float(stock_data["10. change percent"].rstrip('%')) / 100
        }
        
        return stock_info
        
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch stock data")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=5000, reload=True)
