import csv
import os
from datetime import datetime, timedelta

# Sales tax rate
SALES_TAX_RATE = 0.06  # 6%

# Get absolute path for CSV files (adjust this if needed)
BASE_DIR = r"C:\Users\sherra\OneDrive - Sidesys Srl\Escritorio\tesis\Python BYU\semana5"
PRODUCTS_FILE = os.path.join(BASE_DIR, "products.csv")
REQUESTS_FILE = os.path.join(BASE_DIR, "requests.csv")

def read_dictionary(filename, key_column_index):
    """Reads a CSV file and returns a dictionary where the keys are the values of the specified column."""
    dictionary = {}
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")
        
        with open(filename, mode="rt", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) > key_column_index:
                    key = row[key_column_index]
                    dictionary[key] = row
        return dictionary
    except FileNotFoundError as err:
        print(f"❌ Error: {err}")
        exit()
    except PermissionError as err:
        print(f"❌ Error: Permission denied\n{err}")
        exit()

def calculate_total(quantity, price, discount=0):
    """Calculates the total price, applying a discount if necessary."""
    return quantity * price * (1 - discount)

def apply_discount(product_code, quantity, price):
    """Applies a special discount for certain promotional products."""
    if product_code == "D083":  # Example: Buy one, get the second at half price
        pairs = quantity // 2
        odds = quantity % 2
        total = (pairs * price * 1.5) + (odds * price)
        return total
    return quantity * price

def generate_receipt(requests, products_dictionary):
    """Generates the receipt with the products, totals, and taxes."""
    total_items = 0
    subtotal = 0.0

    print("\n=============================")
    print("      🐾 VETCARE CLINIC 🐾")
    print("=============================")
    print("\n📋 Requested Items:")

    for row in requests:
        product_code = row[0]
        quantity = int(row[1])
        try:
            product_info = products_dictionary[product_code]
            product_name = product_info[1]
            price = float(product_info[2])
            total_price = apply_discount(product_code, quantity, price)
            total_items += quantity
            subtotal += total_price
            print(f"{product_name}: {quantity} @ ${price:.2f} - Total: ${total_price:.2f}")
        except KeyError:
            print(f"⚠️ Error: Product with code {product_code} not found in the database.")

    taxes = subtotal * SALES_TAX_RATE
    total = subtotal + taxes

    print("\n-----------------------------")
    print(f"📦 Number of Items: {total_items}")
    print(f"💵 Subtotal: ${subtotal:.2f}")
    print(f"🛒 Sales Tax (6%): ${taxes:.2f}")
    print(f"💳 Total Due: ${total:.2f}")
    print("-----------------------------\n")
    print("🙏 Thank you for choosing VetCare Clinic. 🐶🐱")

    # Print the current date and time
    current_date = datetime.now()
    print(f"🕒 Date and Time of Purchase: {current_date:%a %b %d %I:%M:%S %Y}")

    # Return policy calculation (30 days later)
    return_date = current_date + timedelta(days=30)
    print(f"📅 Return Policy Valid Until: {return_date:%a %b %d %Y}")

    # Days until the next promotion
    promo_date = datetime(current_date.year + 1, 1, 1)
    days_until_promo = (promo_date - current_date).days
    print(f"🎉 {days_until_promo} days left until our Grand New Year's Promotion!\n")

def main():
    """Main function that executes the receipt generation."""
    products_dict = read_dictionary(PRODUCTS_FILE, 0)

    try:
        if not os.path.exists(REQUESTS_FILE):
            raise FileNotFoundError(f"File not found: {REQUESTS_FILE}")
        
        with open(REQUESTS_FILE, mode="rt", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            requests = [row for row in reader if len(row) >= 2]
    except FileNotFoundError as err:
        print(f"❌ Error: {err}")
        exit()
    except PermissionError as err:
        print(f"❌ Error: Permission denied\n{err}")
        exit()

    generate_receipt(requests, products_dict)

if __name__ == "__main__":
    main()