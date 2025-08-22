\
import json
import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret")

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def load_json(name):
    with open(os.path.join(DATA_DIR, name), "r", encoding="utf-8") as f:
        return json.load(f)

# Load datasets at startup
PRODUCTS = load_json("products.json")
SERVICES = load_json("services.json")
RENTALS = load_json("rentals.json")
VENDORS = load_json("vendors.json")
TESTIMONIALS = load_json("testimonials.json")
METRICS = load_json("metrics.json")

def search_and_filter(items, q=None, category=None, min_price=None, max_price=None, city=None):
    def in_range(price):
        if min_price is not None and price < min_price: return False
        if max_price is not None and price > max_price: return False
        return True
    out = []
    for it in items:
        hay = " ".join([str(it.get(k,"")) for k in ["name","description","category","tags"]]).lower()
        ok = True
        if q:
            ok = q.lower() in hay
        if ok and category and category != "all":
            ok = it.get("category") == category
        if ok and (min_price is not None or max_price is not None):
            price = float(it.get("price", 0))
            ok = in_range(price)
        if ok and city:
            v = it.get("city") or it.get("vendor_city")
            ok = (v is None) or (city.lower() in v.lower())
        if ok:
            out.append(it)
    return out

@app.context_processor
def inject_globals():
    cart_count = len(session.get("cart", []))
    compare_count = len(session.get("compare", []))
    return dict(cart_count=cart_count, compare_count=compare_count, metrics=METRICS)

@app.route("/")
def index():
    featured = PRODUCTS[:6]
    return render_template("index.html", featured=featured, testimonials=TESTIMONIALS)

@app.route("/procurement")
def procurement():
    q = request.args.get("q")
    category = request.args.get("category")
    min_price = request.args.get("min_price", type=float)
    max_price = request.args.get("max_price", type=float)
    city = request.args.get("city")
    items = search_and_filter(PRODUCTS, q, category, min_price, max_price, city)
    categories = sorted(set([p["category"] for p in PRODUCTS]))
    return render_template("procurement.html", items=items, categories=categories)

@app.route("/services")
def services():
    q = request.args.get("q")
    category = request.args.get("category")
    city = request.args.get("city")
    items = search_and_filter(SERVICES, q, category, None, None, city)
    categories = sorted(set([s["category"] for s in SERVICES]))
    return render_template("services.html", items=items, categories=categories)

@app.route("/rentals")
def rentals():
    q = request.args.get("q")
    category = request.args.get("category")
    city = request.args.get("city")
    min_price = request.args.get("min_price", type=float)
    max_price = request.args.get("max_price", type=float)
    items = search_and_filter(RENTALS, q, category, min_price, max_price, city)
    categories = sorted(set([r["category"] for r in RENTALS]))
    return render_template("rentals.html", items=items, categories=categories)

@app.route("/vendors")
def vendors():
    q = request.args.get("q")
    city = request.args.get("city")
    items = search_and_filter(VENDORS, q, None, None, None, city)
    return render_template("vendors.html", items=items)

@app.route("/vendors/<vid>")
def vendor_detail(vid):
    v = next((x for x in VENDORS if x["id"] == vid), None)
    if not v: 
        return redirect(url_for("vendors"))
    v_products = [p for p in PRODUCTS if p["vendor_id"] == vid]
    v_services = [s for s in SERVICES if s["vendor_id"] == vid]
    v_rentals = [r for r in RENTALS if r["vendor_id"] == vid]
    return render_template("vendor_detail.html", v=v, v_products=v_products, v_services=v_services, v_rentals=v_rentals)

@app.route("/compare/add/<kind>/<item_id>")
def add_compare(kind, item_id):
    compare = session.get("compare", [])
    compare.append({"kind": kind, "id": item_id})
    session["compare"] = compare[:10]
    flash("Added to comparison.", "success")
    return redirect(request.referrer or url_for("index"))

@app.route("/compare")
def compare():
    compare = session.get("compare", [])
    resolved = []
    for entry in compare:
        if entry["kind"] == "product":
            item = next((p for p in PRODUCTS if p["id"] == entry["id"]), None)
        elif entry["kind"] == "service":
            item = next((s for s in SERVICES if s["id"] == entry["id"]), None)
        else:
            item = next((r for r in RENTALS if r["id"] == entry["id"]), None)
        if item:
            resolved.append({"kind": entry["kind"], **item})
    return render_template("compare.html", items=resolved)

@app.route("/cart/add/<kind>/<item_id>")
def cart_add(kind, item_id):
    cart = session.get("cart", [])
    cart.append({"kind": kind, "id": item_id})
    session["cart"] = cart
    flash("Added to cart.", "success")
    return redirect(request.referrer or url_for("index"))

@app.route("/cart")
def cart_view():
    cart = session.get("cart", [])
    resolved = []
    total = 0.0
    for entry in cart:
        if entry["kind"] == "product":
            item = next((p for p in PRODUCTS if p["id"] == entry["id"]), None)
        elif entry["kind"] == "service":
            item = next((s for s in SERVICES if s["id"] == entry["id"]), None)
        else:
            item = next((r for r in RENTALS if r["id"] == entry["id"]), None)
        if item:
            total += float(item.get("price", 0))
            resolved.append({"kind": entry["kind"], **item})
    return render_template("cart.html", items=resolved, total=total)

@app.route("/checkout", methods=["GET","POST"])
def checkout():
    if request.method == "POST":
        # Simulate checkout success
        session["cart"] = []
        flash("Order placed via escrow (demo). You'll receive an email shortly.", "success")
        return redirect(url_for("index"))
    return render_template("checkout.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        flash("Thanks! We'll get back to you within 24 hours. (Demo)", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")

@app.route("/dashboard")
def dashboard():
    # Simple analytics dashboard from metrics.json
    return render_template("dashboard.html")

@app.route("/api/search")
def api_search():
    q = request.args.get("q", "")
    kind = request.args.get("kind", "all")
    results = []
    if kind in ("all","product"):
        results += search_and_filter(PRODUCTS, q)
    if kind in ("all","service"):
        results += search_and_filter(SERVICES, q)
    if kind in ("all","rental"):
        results += search_and_filter(RENTALS, q)
    return jsonify(results[:25])

if __name__ == "__main__":
    app.run(debug=True)
