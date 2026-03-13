from History import add_to_history #Trae add_to_history de History.py y activa la lista global

def product_records():
    
    #Usa .capitalize() para estandarizar la entrada del usuario
    product = input(">> Please enter the item to register: ").capitalize() 
    try:
        price = float(input(">> Please enter the product price: "))
        quantity = int(input(">> Please enter the quantity of products sold: "))
    except ValueError: #Captura ValueError y reinicia el proceso si hay texto inválido
        print("_"*40)
        print("\nInvalid data. Please enter numbers only.")
        print("_"*40)
        return product_records()
    total = price*quantity #Calcula el total de la operacion.
    

    
   #Arma diccionario con 4 datos 
    producto = {
        "product": product,
        "price": price,
        "quantity": quantity,
        "total": total
    }
    add_to_history(producto) # Llama a add_to_history(producto) para guardar el paquete en la lista global, luego imprime una confirmación
# al usuario con el nombre del producto y el total.
    
    print("_"*40) # Mejora la visualizacion y la experiencia de usuario
    print(f"\n>> {producto['product']} It was correctly registered")
    print(f">> The total amount raised was: ${producto['total']}")
    print("_"*40) # Mejora la visualizacion y la experiencia de usuario
    