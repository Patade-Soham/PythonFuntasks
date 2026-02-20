from flask import Flask, render_template, request, redirect, url_for, session, flash
from decimal import Decimal
from products import PRODUCTS, CATEGORIES

app = Flask(__name__)
app.secret_key = "change-this-in-production"  # required for session


def _get_cart():
    cart = session.get("cart", {})
    # cart structure: { product_id(str): quantity(int), ... }
    return cart

def _save_cart(cart):
    session["cart"] = cart

def _cart_items_and_total():
    cart = _get_cart()
    items = []
    total = Decimal("0.00")
    for pid_str, qty in cart.items():
        try:
            pid = int(pid_str)
        except ValueError:
            continue
        product = next((p for p in PRODUCTS if p["id"] == pid), None)
        if not product:
            continue
        line_total = Decimal(str(product["price"])) * qty
        total += line_total
        items.append({
            "product": product,
            "quantity": qty,
            "line_total": float(line_total)
        })
    return items, float(total)

# ---------- Routes ----------
@app.route("/")
def shop():
    # Filter by category via query param: /?category=Fruits
    category = request.args.get("category", "All")
    if category == "All":
        filtered = PRODUCTS
    else:
        filtered = [p for p in PRODUCTS if p["category"] == category]

    # Count total items in cart (sum of quantities)
    total_items = sum(_get_cart().values())
    return render_template(
        "shop.html",
        products=filtered,
        categories=CATEGORIES,
        selected_category=category,
        total_items=total_items
    )

@app.post("/add")
def add_to_cart():
    product_id = request.form.get("product_id")
    if not product_id:
        flash("Invalid product.", "error")
        return redirect(url_for("shop"))

    cart = _get_cart()
    cart[product_id] = cart.get(product_id, 0) + 1
    _save_cart(cart)
    flash("Item added to cart.", "success")
    return redirect(request.referrer or url_for("shop"))

@app.route("/cart")
def cart_view():
    items, total = _cart_items_and_total()
    total_items = sum(_get_cart().values())
    return render_template(
        "cart.html",
        items=items,
        total=total,
        total_items=total_items
    )

@app.post("/cart/update")
def cart_update():
    pid = request.form.get("product_id")
    action = request.form.get("action")  # "inc", "dec", "remove"
    cart = _get_cart()
    if pid not in cart:
        return redirect(url_for("cart_view"))

    if action == "inc":
        cart[pid] += 1
    elif action == "dec":
        cart[pid] -= 1
        if cart[pid] <= 0:
            cart.pop(pid, None)
    elif action == "remove":
        cart.pop(pid, None)

    _save_cart(cart)
    return redirect(url_for("cart_view"))

@app.post("/checkout")
def checkout():
    cart = _get_cart()
    if not cart:
        flash("Your cart is empty.", "error")
        return redirect(url_for("shop"))

    items, total = _cart_items_and_total()

    # Clear cart after "placing" order
    session["cart"] = {}

    return render_template("checkout.html", total=total)

# Optional: simple API endpoints (if you later want a SPA frontend)
@app.get("/api/products")
def api_products():
    return {"products": PRODUCTS}

@app.get("/api/cart")
def api_cart():
    items, total = _cart_items_and_total()
    return {"items": items, "total": total}

if __name__ == "__main__":
    app.run(debug=True)

