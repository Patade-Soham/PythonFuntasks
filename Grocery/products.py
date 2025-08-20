# products.py
PRODUCTS = [
    {"id": 1, "name": "Organic Apples", "price": 1.50, "image": "https://placehold.co/100x100/A8D1A8/ffffff?text=Apples", "category": "Fruits"},
    {"id": 2, "name": "Fresh Bananas", "price": 0.75, "image": "https://placehold.co/100x100/F5D76E/000000?text=Bananas", "category": "Fruits"},
    {"id": 3, "name": "Cherry Tomatoes", "price": 2.25, "image": "https://placehold.co/100x100/E86851/ffffff?text=Tomatoes", "category": "Vegetables"},
    {"id": 4, "name": "Spinach", "price": 1.99, "image": "https://placehold.co/100x100/4CAF50/ffffff?text=Spinach", "category": "Vegetables"},
    {"id": 5, "name": "Whole Milk", "price": 3.49, "image": "https://placehold.co/100x100/ADD8E6/000000?text=Milk", "category": "Dairy"},
    {"id": 6, "name": "Cheddar Cheese", "price": 4.99, "image": "https://placehold.co/100x100/F0B27A/000000?text=Cheese", "category": "Dairy"},
    {"id": 7, "name": "Artisan Bread", "price": 2.75, "image": "https://placehold.co/100x100/D2B48C/000000?text=Bread", "category": "Bakery"},
    {"id": 8, "name": "Eggs (dozen)", "price": 3.99, "image": "https://placehold.co/100x100/F4E3C4/000000?text=Eggs", "category": "Dairy"},
]

CATEGORIES = ["All"] + sorted(list({p["category"] for p in PRODUCTS}))
