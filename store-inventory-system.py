# error handling: raising custom exceptions

class OutOfStockError (Exception):
    """Custom exception raised when stock is insufficient for a sale."""
    pass


# oop: defining classes, objects, and methods

class Product:
    def __init__(self, product_id, name, price, stock_level):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_level = stock_level
    
    def restock(self, amount):
        self.stock_level += amount
    
    def display_info(self):
        return f"[{self.product_id}] {self.name} - ${self.price} | Stock: {self.stock_level}"

class Store:
    def __init__(self):
        # basic syntax: dictionaries, sets, and lists
        self.catalog = {}
        self.categories = set()
        self.sales_history = []

    def add_product(self, product, category="General"):
        # add to dictionary and set
        self.catalog[product.product_id] = product
        self.categories.add(category)
        print(f"Added {product.name} to the store under '{category}'.")
 
    def sell_product(self, product_id, quantity):
        if quantity <= 0:
            raise ValueError("Sale quantity must be 1 or greater.")
        
        try:
            product = self.catalog[product_id]

            if product.stock_level < quantity:
                raise OutOfStockError(f"Cannot sell {quantity} of {product.name}. Only {product.stock_level} left.")
            
            product.stock_level -= quantity

            transaction_record = ("SALE", product.name, quantity, product.price*quantity)

            self.sales_history.append(transaction_record)
            print(f"Successfully sold {quantity}x {product.name}.")

        except KeyError:
            print(f"Sale Failed: Product ID '{product_id}' does not exist.")
        except OutOfStockError as e:
            print(f"Sale Failed: {e}")
        except ValueError as e:
            print(f"Sale Failed: {e}")

    def show_inventory(self):
        print("\n--- Current Inventory ---")
        for prod_id, product in self.catalog.items():
            print(product.display_info())

        print(f"Availale Categories: {', '.join(self.categories)}")

    def run_daily_summary(self):
        print("\n--- Daily Summary ---")
        total_revenue = 0
        transactions_processed = 0

        while transactions_processed < len(self.sales_history):
            action, name, qty, total_price = self.sales_history[transactions_processed]
            total_revenue+=total_price
            transactions_processed+=1

        print(f"Total Transactions: {transactions_processed}")
        print(f"Total Revenue: ${total_revenue:.2f}")

# main execution script
if __name__ == "__main__":
    # creating a store object
    my_store = Store()

    #creating product objects
    p1 = Product(product_id="T001", name="Wireless Mouse", price=25.00, stock_level=10)
    p2 = Product(product_id="T002", name="Mechanical Keyboard", price=85.00, stock_level=3)

    my_store.add_product(p1, category="Electronics")
    my_store.add_product(p2, category="Electronics")

    print('\n--- Processing Sales ---')
    my_store.sell_product("T001", 2)

    my_store.sell_product("T002", 5)

    my_store.sell_product("X999", 1)

    try:
        my_store.sell_product("T001", -3)
    except ValueError as e:
        print("Caught an error in main script: {e}")

    my_store.show_inventory()
    my_store.run_daily_summary()


