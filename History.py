from History import add_to_history

def product_records():
    
    product = input(">> Please enter the item to register: ").capitalize()
    try:
        price = float(input(">> Please enter the product price: "))
        quantity = int(input(">> Please enter the quantity of products sold: "))
    except ValueError:
        print("_"*40)
        print("\nInvalid data. Please enter numbers only.")
        print("_"*40)
        return product_records()
    total = price*quantity
    

    
    
    producto = {
        "product": product,
        "price": price,
        "quantity": quantity,
        "total": total
    }
    add_to_history(producto)
    
    print("_"*40)
    print(f"\n>> {producto['product']} It was correctly registered")
    print(f">> The total amount raised was: ${producto['total']}")
    print("_"*40)
    