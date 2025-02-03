from formula import parse_formula  # ✅ Corrección: importar desde formula.py

# Índices de la tabla periódica
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Índices de la lista de símbolos y cantidades
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def make_periodic_table():
    """Crear y devolver un diccionario con los elementos de la tabla periódica."""
    periodic_table_dict = {
        "H": ["Hydrogen", 1.00794],
        "He": ["Helium", 4.002602],
        "Li": ["Lithium", 6.941],
        "Be": ["Beryllium", 9.012182],
        "B": ["Boron", 10.811],
        "C": ["Carbon", 12.0107],
        "N": ["Nitrogen", 14.0067],
        "O": ["Oxygen", 15.9994],
        "F": ["Fluorine", 18.9984032],
        "Ne": ["Neon", 20.1797],
        "Na": ["Sodium", 22.98976928],
        "Mg": ["Magnesium", 24.305],
        "Al": ["Aluminum", 26.9815386],
        "Si": ["Silicon", 28.0855],
        "P": ["Phosphorus", 30.973762],
        "S": ["Sulfur", 32.065],
        "Cl": ["Chlorine", 35.453],
        "K": ["Potassium", 39.0983],
        "Ar": ["Argon", 39.948],
        "Ca": ["Calcium", 40.078],
        "Ti": ["Titanium", 47.867],
        "Fe": ["Iron", 55.845],
        "Ni": ["Nickel", 58.6934],
        "Cu": ["Copper", 63.546],
        "Zn": ["Zinc", 65.38],
        "Ag": ["Silver", 107.8682],
        "I": ["Iodine", 126.90447],
        "Au": ["Gold", 196.966569]
    }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Calcular y devolver la masa molar total de todos los elementos en symbol_quantity_list."""
    total_molar_mass = 0

    for symbol, quantity in symbol_quantity_list:
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_molar_mass += atomic_mass * quantity

    return total_molar_mass

def main():
    """Función principal para calcular la masa molar de un compuesto químico."""
    # Obtener la fórmula molecular del usuario
    formula = input("Enter the molecular formula of the sample: ")

    # Obtener la masa en gramos de la muestra
    sample_mass = float(input("Enter the mass in grams of the sample: "))

    # Crear la tabla periódica
    periodic_table = make_periodic_table()

    # Analizar la fórmula química
    symbol_quantity_list = parse_formula(formula, periodic_table)

    # Calcular la masa molar
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

    # Calcular el número de moles
    number_of_moles = sample_mass / molar_mass

    # Imprimir resultados
    print(f"{molar_mass:.5f} grams/mole")
    print(f"{number_of_moles:.5f} moles")

if __name__ == "__main__":
    main()