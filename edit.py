import json
import os

PRODUCTS_FILE = r'teknobuild\products.json'

def load_products():
    if not os.path.exists(PRODUCTS_FILE):
        return []
    with open(PRODUCTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_products(products):
    with open(PRODUCTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

def list_products(products):
    if not products:
        print("No products found.")
        return
    for idx, p in enumerate(products, 1):
        print(f"{idx}. {p['name']} ({p['price']})")

def add_product(products):
    name = input("Product name: ")
    price = input("Price (e.g., ₹350): ")
    images = []
    while True:
        img = input("Add image URL (leave blank to finish): ")
        if not img:
            break
        images.append(img)
    features = []
    while True:
        feat = input("Add feature (leave blank to finish): ")
        if not feat:
            break
        features.append(feat)
    products.append({
        "name": name,
        "price": price,
        "images": images,
        "features": features
    })
    print("Product added.")

def edit_product(products):
    list_products(products)
    idx = int(input("Enter product number to edit: ")) - 1
    if 0 <= idx < len(products):
        p = products[idx]
        print(f"Editing {p['name']}")
        p['name'] = input(f"Name [{p['name']}]: ") or p['name']
        p['price'] = input(f"Price [{p['price']}]: ") or p['price']
        print("Current images:", p['images'])
        if input("Edit images? (y/n): ").lower() == 'y':
            p['images'] = []
            while True:
                img = input("Add image URL (leave blank to finish): ")
                if not img:
                    break
                p['images'].append(img)
        print("Current features:", p['features'])
        if input("Edit features? (y/n): ").lower() == 'y':
            p['features'] = []
            while True:
                feat = input("Add feature (leave blank to finish): ")
                if not feat:
                    break
                p['features'].append(feat)
        print("Product updated.")
    else:
        print("Invalid product number.")

def delete_product(products):
    list_products(products)
    idx = int(input("Enter product number to delete: ")) - 1
    if 0 <= idx < len(products):
        del products[idx]
        print("Product deleted.")
    else:
        print("Invalid product number.")

def main():
    products = load_products()
    while True:
        print("\nProduct Manager Menu:")
        print("1. List products")
        print("2. Add product")
        print("3. Edit product")
        print("4. Delete product")
        print("5. Save and exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_products(products)
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            edit_product(products)
        elif choice == '4':
            delete_product(products)
        elif choice == '5':
            save_products(products)
            print("Changes saved. Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()