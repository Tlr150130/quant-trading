import os

# config.py
# Configuration template for quant-trading project


# API Keys
API_KEY = os.getenv("API_KEY", "your_api_key_here")
API_SECRET = os.getenv("API_SECRET", "your_api_secret_here")

# Project Paths
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC_DIR = os.path.join(PROJECT_DIR, 'src')
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
MODELS_DIR = os.path.join(PROJECT_DIR, 'models')
LOGS_DIR = os.path.join(PROJECT_DIR, 'logs')
CONFIG_DIR = os.path.join(PROJECT_DIR, 'config')

# Trading settings
TRADING_SYMBOL = "BTCUSD"
TRADE_AMOUNT = 0.01
MAX_OPEN_TRADES = 5

# Data source settings
DATA_PROVIDER = "binance"
DATA_REFRESH_INTERVAL = 60  # seconds

# Logging settings
LOG_LEVEL = "INFO"
LOG_FILE = "logs/trading.log"

# Database settings
DB_URI = "sqlite:///trading.db"

# Risk management
MAX_RISK_PER_TRADE = 0.02  # 2% of account

# Add more configuration variables as needed