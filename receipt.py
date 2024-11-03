import csv
from datetime import datetime

# Constants
SALES_TAX_RATE = 0.06

# Function to read the products CSV file
def read_products(file_name):
    products_dict = {}
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                prod_id = row[0]
                name = row[1]
                price = float(row[2])
                products_dict[prod_id] = [name, price]
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        return None
    except PermissionError as e:
        print("Error: permission denied")
        print(e)
        return None
    return products_dict

# Function to read the requests CSV file
def read_requests(file_name):
    requests_list = []
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                prod_id = row[0]
                quantity = int(row[1])
                requests_list.append([prod_id, quantity])
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        return None
    except PermissionError as e:
        print("Error: permission denied")
        print(e)
        return None
    return requests_list

# Function to generate the receipt
def generate_receipt(products_dict, requests_list):
    print("Inkom Emporium")
    
    total_items = 0
    subtotal = 0

    try:
        for request in requests_list:
            prod_id = request[0]
            quantity = request[1]

            # Check for invalid product IDs
            if prod_id not in products_dict:
                raise KeyError(f"Error: unknown product ID '{prod_id}' in the request file")
            
            product_name = products_dict[prod_id][0]
            product_price = products_dict[prod_id][1]
            
            total_items += quantity
            subtotal += product_price * quantity

            print(f"{product_name}: {quantity} @ {product_price:.2f}")
        
        # Calculate sales tax and total
        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax

        # Print totals and thank you message
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print("Thank you for shopping at the Inkom Emporium.")

        # Print current date and time
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a %b %d %Y %I:%M:%S %p}")

    except KeyError as e:
        print(e)

# Main function
def main():
    # File names
    products_file = 'products.csv'
    request_file = 'request.csv'

    # Read products and requests
    products_dict = read_products(products_file)
    requests_list = read_requests(request_file)

    if products_dict is not None and requests_list is not None:
        generate_receipt(products_dict, requests_list)

# Call the main function
if __name__ == "__main__":
    main()
