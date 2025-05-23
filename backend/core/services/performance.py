import yfinance as yf
from loguru import logger

def get_current_market_price(ticker: object) -> float:
    try:
        price = yf.Ticker(ticker)
        logger.info(f"Fetched market price for {ticker}: {price.history(period='1d')['Close'].iloc[-1]}")
        return  price.history(period="1d")['Close'].iloc[-1]
    except Exception as e:
        print(f"Error fetching market price for {ticker}: {str(e)}")
        return 0


def calculate_portfolio_value(portfolio):
    total_value = 0
    for position in portfolio.positions.all():
        market_price = get_current_market_price(position.asset.ticker) if position.asset.ticker else float(position.price_at_buy)
        total_value += int(position.quantity) * int(market_price)
    return total_value
