from History import add_to_history  # Imports add_to_history from History.py and uses the global list


def product_records():
    
    # Uses .capitalize() to standardize user input
    product = input(">> Please enter the item to register: ").capitalize()
    
    try:
        price = float(input(">> Please enter the product price: "))
        quantity = int(input(">> Please enter the quantity of products sold: "))
    except ValueError:  # Catches ValueError and restarts the process if invalid input is entered
        print("_" * 40)
        print("\nInvalid data. Please enter numbers only.")
        print("_" * 40)
        return product_records()
    
    total = price * quantity  # Calculates the total of the operation

    # Builds a dictionary with 4 data points
    product_data = {
        "product": product,
        "price": price,
        "quantity": quantity,
        "total": total
    }

    # Calls add_to_history(product_data) to store it in the global list,
    # then prints a confirmation to the user
    add_to_history(product_data)
    
    print("_" * 40)  # Improves visualization and user experience
    print(f"\n>> {product_data['product']} was successfully registered")
    print(f">> The total amount earned was: ${product_data['total']}")
    print("_" * 40)  # Improves visualization and user experience
