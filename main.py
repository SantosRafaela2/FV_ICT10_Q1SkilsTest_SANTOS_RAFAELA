from flask import Flask, render_template, request

app = Flask(__name__)

# Menu with prices
menu = {
    "Carbonara": 120,
    "Garlic Bread": 50,
    "Caesar Salad": 100,
    "Iced Tea": 80,
    "Sparkling Water": 60
}

@app.route("/", methods=["GET", "POST"])
def index():
    total = 0
    items = []
    name = ""
    address = ""
    contact = ""

    if request.method == "POST":
        # Get customer info
        name = request.form["name"]
        address = request.form["address"]
        contact = request.form["contact"]

        # Get selected menu items
        chosen = request.form.getlist("items")
        for food in chosen:
            items.append(food)
            total += menu[food]

    return render_template("index.html", 
                           menu=menu, 
                           items=items, 
                           total=total, 
                           name=name, 
                           address=address, 
                           contact=contact)

if __name__ == "__main__":
    app.run(debug=True)
