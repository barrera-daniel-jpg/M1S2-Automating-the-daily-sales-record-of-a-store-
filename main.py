from History import show_summary
from Login import product_records

print("="*24)
print("| WELCOME TO THE SYSTEM |")
print("="*24)

def request_option():
    opcion = input("\nAre you going to register products? (Y/N): ").upper()
    if opcion not in ['Y', 'N']:
        print(" Invalid option, please try again (Y/N)")
        return request_option()  
    return opcion

while request_option() == 'Y':
    product_records()
show_summary()
print("The program has ended. Thank you for your registrations.")