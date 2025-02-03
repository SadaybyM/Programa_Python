import csv

# Cargar y analizar el archivo products.csv
products_file_path = "products.csv"
request_file_path = "request.csv"

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.
    
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    
    Return: a compound dictionary that contains the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, mode="rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Saltar la primera fila (encabezados)

        for row in reader:
            if len(row) > key_column_index:  # Verifica que la fila tenga suficientes columnas
                key = row[key_column_index]
                dictionary[key] = row

    return dictionary

# Verificar si se carga correctamente el diccionario de productos
products_dict = read_dictionary(products_file_path, 0)
products_dict


def main():
    """Procesa los archivos CSV y genera un recibo"""
    # Leer el archivo products.csv en un diccionario
    products_dict = read_dictionary("products.csv", 0)
    
    print("All Products")
    print(products_dict)  # Imprime el diccionario para verificar que se leyó bien

    # Abrir el archivo request.csv
    with open("request.csv", mode="rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)  # Saltar la primera fila (encabezado)

        print("\nRequested Items")

        for row in reader:
            product_number = row[0]  # Código del producto
            quantity = int(row[1])   # Cantidad solicitada

            # Buscar el producto en el diccionario
            if product_number in products_dict:
                product_name = products_dict[product_number][1]
                price = float(products_dict[product_number][2])
                print(f"{product_name}: {quantity} @ {price:.2f}")
            else:
                print(f"Error: Producto {product_number} no encontrado.")

if __name__ == "__main__":
    main()