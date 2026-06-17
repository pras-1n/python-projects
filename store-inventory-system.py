# error handling: raising custom exceptions

class OutOfStockError (Exception):
    """Custom exception raised when stock is insufficient for a sale."""
    pass