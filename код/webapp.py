from flask import Flask, render_template

app = Flask(__name__)

phones = [
    {"name": "iPhone 15 Pro", "price": 1200, "img": "https://store.storeimages.cdn-apple.com/iphone15.jpg"},
    {"name": "Samsung Galaxy S24", "price": 1000, "img": "https://example.com/s24.jpg"},
    {"name": "Xiaomi 14", "price": 800, "img": "https://example.com/xiaomi14.jpg"},
]

@app.route("/catalog")
def catalog():
    return render_template("catalog.html", phones=phones)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
