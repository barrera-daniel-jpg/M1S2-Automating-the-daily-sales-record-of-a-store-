from History import show_summary 
from Login import product_records
# Trae las dos funciones principales de sus respectivos módulos.

print("="*24) # Mejora la visualizacion y la experiencia de usuario
print("| WELCOME TO THE SYSTEM |")
print("="*24) # Mejora la visualizacion y la experiencia de usuario

def request_option():
    opcion = input("\nAre you going to register products? (Y/N): ").upper() 
    if opcion not in ['Y', 'N']:
        print(" Invalid option, please try again (Y/N)")
        return request_option()  
    return opcion
# () La función validadora. Solo acepta Y o N 
# — cualquier otra cosa activa la recursión y vuelve a preguntar. 
# Retorna la opción válida al while.

while request_option() == 'Y': 
    product_records() 
show_summary() 
print("The program has ended. Thank you for your registrations.")
#Una vez fuera del bucle, estas dos líneas se ejecutan una sola vez.