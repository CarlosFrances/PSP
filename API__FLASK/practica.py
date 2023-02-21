from flask import Flask, jsonify, request


application = Flask(__name__)

from products import products




"""@application.route("/get-users/<user>") # endpoint + ruta nos sacará la edad
def get_users(user):

    return user"""

@application.route("/a/<string:a>/<string:e>",methods=["GET"])
def get_a(a,e):
    return a+e

@application.route("/ping")
def ping():
    return jsonify({"message":"Pong!"})

@application.route("/products")
def get_products():
    return jsonify({"products":products,"message":"Product list"})

@application.route("/products/<string:product_name>")
def get_product(product_name):
    productsFound = [product for product in products if product["name"] == product_name]
    if len(productsFound) > 0:
        return jsonify({"product":productsFound[0]})
    return jsonify({"message":"product not found"})

@application.route("/products", methods=["POST"])
def addProduct():
    new_product = {
        "name":request.json["name"],
        "price":request.json["price"],
        "quantity":request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"message":"Product added succesfully", "products":products})

@application.route("/products/<string:product_name>",methods=["PUT"])
def edit_product(product_name):
    productFound = [product for product in products if product["name"] == product_name]
    if len(productFound) > 0:
        productFound[0]["name"] = request.json["name"]
        productFound[0]["price"] = request.json["price"]
        productFound[0]["quantity"] = request.json["quantity"]
        return jsonify({
            "message":"Product updated",
            "product":productFound[0]
        })
    return jsonify({"message":"Product not found"})

@application.route("/products/<string:product_name>",methods=["DELETE"])
def delete_product(product_name):
    productFound = [product for product in products if product["name"] == product_name]
    if len(productFound) > 0:
        products.remove(productFound[0])
        return jsonify({"message":"Product deleted",
                        "products":products})
    return jsonify({"message":"Product not found"})

if __name__ == "__main__":
    application.run(debug=True,port=5000)