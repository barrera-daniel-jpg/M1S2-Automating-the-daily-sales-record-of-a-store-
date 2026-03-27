history = []  # Global list that acts as the program's memory


def add_to_history(product):  # Receives dictionaries from Login.py and stores them using append()
    history.append(product)


def show_summary():  # Iterates through the list, prints products, and accumulates totals
    
    print("\n=========== Sales Summary ===========")  # Improves visualization and user experience
    total_memory = 0
    
    for product in history:
        print(f">> {product['product']}: {product['quantity']} quantity x ${product['price']} = ${product['total']}")
        total_memory += product['total']
    
    print(f">> Total earned: ${total_memory}")
    print("=" * 40)  # Improves visualization and user experience
