# Automating-the-daily-sales-record-of-a-store-

This is the repository where the code for a system that automates a store's daily sales records from the terminal is hosted. 
>### FLOW CHART:


![Flow_chart](https://github.com/user-attachments/assets/8ff763bc-d8b2-43c4-a3bf-a78725a4f872)

## Implemented strategy 
#### The strategy implemented consisted of first creating a simple flowchart that would allow the system's entry point to be visualized, without implementing many conditions. Subsequently, three files were created, one of which was the main file (the brain of the program). Once created, functions were defined in each .py file, providing a clear perspective of how the code is executed depending on where the functions and their respective imports are defined.
#### Within the functions, some variables were defined which, in turn, became inputs so that the user could define which items to register. Therefore, after defining variables, functions, and evaluating errors, among other aspects, the imports were carried out together with several print statements within the main file, thus generating a readable interface for the user. 

> Traducción:
 >> La estrategia implementada consistió en crear, primero, un diagrama de flujo sencillo que permitiera visualizar el punto de entrada del sistema, sin implementar muchas condiciones. Posteriormente, se crearon 3 archivos, uno de los cuales era el main (el cerebro del programa); una vez creados, se definieron funciones en cada archivo .py, lo que permite tener una perspectiva clara de cómo se ejecuta el código dependiendo de dónde estén definidas las funciones y sus respectivas importaciones.

>> Dentro de las funciones se definieron algunas variables que, a su vez, se convirtieron en entradas (inputs) para que el usuario sea el encargado de definir qué artículos va a registrar. Por consiguiente, después de haber definido variables, funciones y evaluado errores, entre otros aspectos, se procedió a realizar las importaciones junto con varios print dentro del main, generando así una interfaz legible para el usuario.

## Code explanation:

 ### History.py:
> * History.py is the program's memory.
> * It contains a global list history = [] that stores the dictionary containing the product details.
>* The file has two functions: add_to_history(), which receives the product characteristics and adds them to the global list, and show_summary(), which iterates through that list at the end and prints a summary of each product with its cumulative total.

### Login.py:
>* Login.py is where all user interaction takes place. It has a single function, product_records(), containing a sequence of 5 steps:
>* It prompts the user for the product name using an input field labeled “product name” (capitalize()), then validates that the price and quantity are numbers and not text strings using try/except ValueError — if they are not, it calls itself recursively, prompting the user for the data again, then calculates the total = price * quantity to determine the total profit, and finally packages the four data points into a dictionary and sends it to add_to_history().

### main.py:
>* main.py is the coordinator. 
>* It imports the functions from the other two files, prints the welcome message, and controls the flow with two key elements: request_option(), which validates that the user enters Y or N using recursion, and the while loop request_option() == ‘Y’, which keeps the program running as long as the user wants to continue adding products. When the user responds with N, the loop ends and show_summary() is executed, creating the summary and terminating the program.
