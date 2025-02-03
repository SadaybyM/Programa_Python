from formula import parse_formula  # Importar desde formula.py

def make_periodic_table():
    """Crear y devolver un diccionario con los elementos de la tabla periódica."""
    periodic_table_dict = {
        "H": ["Hydrogen", 1.00794, 1],
        "He": ["Helium", 4.002602, 2],
        "Li": ["Lithium", 6.941, 3],
        "Be": ["Beryllium", 9.012182, 4],
        "B": ["Boron", 10.811, 5],
        "C": ["Carbon", 12.0107, 6],
        "N": ["Nitrogen", 14.0067, 7],
        "O": ["Oxygen", 15.9994, 8],
        "F": ["Fluorine", 18.9984032, 9],
        "Ne": ["Neon", 20.1797, 10],
        "Na": ["Sodium", 22.98976928, 11],
        "Mg": ["Magnesium", 24.305, 12],
        "Al": ["Aluminum", 26.9815386, 13],
        "Si": ["Silicon", 28.0855, 14],
        "P": ["Phosphorus", 30.973762, 15],
        "S": ["Sulfur", 32.065, 16],
        "Cl": ["Chlorine", 35.453, 17],
        "K": ["Potassium", 39.0983, 19],
        "Ca": ["Calcium", 40.078, 20],
        "Fe": ["Iron", 55.845, 26],
        "Cu": ["Copper", 63.546, 29],
        "Zn": ["Zinc", 65.38, 30],
        "Ag": ["Silver", 107.8682, 47],
        "I": ["Iodine", 126.90447, 53],
        "Au": ["Gold", 196.966569, 79]
    }
    return periodic_table_dict

# Índices para acceder a los datos en el diccionario
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
ATOMIC_NUMBER_INDEX = 2  # Nuevo índice para contar protones

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Calcular y devolver la masa molar total de los elementos en symbol_quantity_list."""
    total_molar_mass = 0
    for symbol, quantity in symbol_quantity_list:
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_molar_mass += atomic_mass * quantity
    return total_molar_mass

def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Calcular y devolver el número total de protones en una molécula."""
    total_protons = 0
    for symbol, quantity in symbol_quantity_list:
        atomic_number = periodic_table_dict[symbol][ATOMIC_NUMBER_INDEX]
        total_protons += atomic_number * quantity
    return total_protons

def get_formula_name(formula, known_molecules_dict):
    """Buscar el nombre de una fórmula química en un diccionario de moléculas conocidas."""
    return known_molecules_dict.get(formula, "Unknown Compound")

def main():
    """Función principal para calcular la masa molar de un compuesto químico."""
    # Diccionario de moléculas conocidas
    known_molecules_dict = {
        "H2O": "Water",
        "C6H12O6": "Glucose",
        "CH4": "Methane",
        "C2H6O": "Ethanol",
        "CO2": "Carbon Dioxide",
        "O2": "Oxygen Gas"
    }

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

    # Obtener el nombre de la fórmula si es conocida
    formula_name = get_formula_name(formula, known_molecules_dict)

    # Calcular el número de protones
    total_protons = sum_protons(symbol_quantity_list, periodic_table)

    # Imprimir resultados
    print(f"\nFormula Name: {formula_name}")
    print(f"Molar Mass: {molar_mass:.5f} grams/mole")
    print(f"Number of Moles: {number_of_moles:.5f} moles")
    print(f"Total Protons: {total_protons}")

if __name__ == "__main__":
    main()