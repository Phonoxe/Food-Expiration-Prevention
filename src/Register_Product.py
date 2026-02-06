import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "data.json"

if DATA_FILE.exists():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        products = json.load(f)
else:
    products = []

product_name = input("Enter product name : ")

while True:
    input_expiry_date = input("Enter Expiry Date (DD/MM/YYYY) : ")
    try:
        product_expiry_date = datetime.strptime(input_expiry_date, "%d/%m/%Y").date()
        break
    except ValueError:
        print("Retry. Invalid format. Example : 12/07/2009")

new_product = {"Name": product_name, "Date": product_expiry_date.strftime("%d/%m/%Y")}

products.append(new_product)

with open(DATA_FILE, "w", encoding="utf-8") as file:
    json.dump(products, file)
