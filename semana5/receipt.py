"""
GROCERY STORE RECEIPT PROJECT - CSE 111
=========================================
This program processes grocery store orders and generates a detailed receipt.
Added enhancements:
✅ Implemented "Buy one, get the second one at half price" discount for yogurt (D083).
✅ Displays the number of days until the New Year's Sale.
✅ Shows the return deadline (30 days after the purchase).
"""

import csv
from datetime import datetime, timedelta

# Define the sales tax rate
SALES_TAX_RATE = 0.06
DISCOUNT_PRODUCT = "D083"  # Product code for the discount (yogurt)

def read_dictionary(filename, key_column_index):
    """Reads a CSV file and stores it in a dictionary.

    Parameters:
        filename: Name of the CSV file.
        key_column_index: Index of the column to use as the key in the dictionary.

    Returns:
        A dictionary where the keys are the values from the `key_column_index` column,
        and the values are lists containing product information.
    """
    dictionary = {}

    try:
        with open(filename, mode="rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the first row (headers)

            for row in reader:
                if len(row) > key_column_index:  # Avoid empty rows
                    key = row[key_column_index]
                    dictionary[key] = row

        return dictionary
    except FileNotFoundError as err:
        print(f"Error: missing file\n{err}")
        exit()
    except PermissionError as err:
        print(f"Error: permission denied\n{err}")
        exit()

def calculate_discounted_price(quantity, price):
    """Calculates the total price applying the 'buy one, get the second one at half price' discount.

    Parameters:
        quantity: Number of products purchased.
        price: Unit price of the product.

    Returns:
        Total price with the discount applied.
    """
    full_price_count = quantity // 2 + quantity % 2  # Items at full price
    half_price_count = quantity // 2  # Items at half price
    total_price = (full_price_count * price) + (half_price_count * (price / 2))
    return total_price

def main():
    """Main function that processes the order and generates the receipt."""
    
    # Attempt to read the products file
    products_dict = read_dictionary("products.csv", 0)

    # Initialize variables for calculations
    total_items = 0
    subtotal = 0.0

    print("\n=============================")
    print("       INKOM EMPORIUM")
    print("=============================\n")

    print("Requested Items:")
    
    try:
        # Read the request file
        with open("request.csv", mode="rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip headers

            for row in reader:
                if len(row) < 2:  # Verify that the row has enough data
                    continue

                product_number = row[0]
                quantity = int(row[1])

                # Retrieve product information from the dictionary
                product_info = products_dict[product_number]  # May raise KeyError
                product_name = product_info[1]
                price = float(product_info[2])

                # Apply discount if the product is D083 (yogurt)
                if product_number == DISCOUNT_PRODUCT:
                    total_price = calculate_discounted_price(quantity, price)
                    print(f"{product_name}: {quantity} @ ${price:.2f} (Discount applied)")
                else:
                    total_price = quantity * price
                    print(f"{product_name}: {quantity} @ ${price:.2f}")

                # Accumulate total number of items and subtotal
                total_items += quantity
                subtotal += total_price

    except KeyError as err:
        print(f"\nError: unknown product ID in the request.csv file\n{err}")
        exit()
    except FileNotFoundError as err:
        print(f"\nError: missing file\n{err}")
        exit()
    except PermissionError as err:
        print(f"\nError: permission denied\n{err}")
        exit()
    except ValueError as err:
        print(f"\nError: invalid data format\n{err}")
        exit()

    # Calculate sales tax and total
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

    print("\n-----------------------------")
    print(f"Number of Items: {total_items}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("-----------------------------\n")

    print("Thank you for shopping at the Inkom Emporium.")

    # Get the current date and time
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")

    # Show the number of days until New Year's Sale
    new_year = datetime(current_date_and_time.year + 1, 1, 1)
    days_until_new_year = (new_year - current_date_and_time).days
    print(f"📅 {days_until_new_year} days until the New Year's Sale!")

    # Show the return deadline (30 days after the purchase)
    return_date = current_date_and_time + timedelta(days=30)
    print(f"🔄 You can return items until: {return_date:%a %b %d %I:%M:%S %Y}")

if __name__ == "__main__":
    main()