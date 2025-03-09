from flask import Flask, request, jsonify
from flask_cors import CORS
import defect_detect
import try_on
import return_flow_opt
import price_search
import description_conversion
from PIL import Image
import cv2
import numpy as np
import io
import base64

app = Flask(__name__)
CORS(app)

users = {"test@example.com": "password123"}  # Sample user data
orders = [
    {
        "id": 1,
        "item": "Women's Hydrenalite™ Down A-Line Vest",
        "price": 139.99,
        "status": "Delivered",
    }
]


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    if users.get(email) == password:
        return jsonify({"success": True, "message": "Login successful"})
    return jsonify({"success": False, "message": "Invalid credentials"}), 401


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)


@app.route("/return", methods=["POST"])
def process_return():
    data = request.json
    order_id = data.get("order_id")
    reason = data.get("reason")
    return jsonify(
        {
            "success": True,
            "message": f"Return request for order {order_id} processed",
            "reason": reason,
        }
    )


@app.route("/defect-detection", methods=["POST"])
def defect_detection():
    data = request.json

    if "product_img" not in request.files:
        return jsonify({"error": "No product image"}), 400

    product_img = request.files["product_img"]
    if product_img.filename == "":
        return jsonify({"error": "No selected file"}), 400

    product_img = product_img.read() ## byte file
    npimg = np.fromstring(product_img, np.uint8)
    product_img = cv2.imdecode(npimg,cv2.IMREAD_COLOR)
    product_img = Image.fromarray(product_img.astype("uint8"))

    product_title = data.get("product_title")
    product_description = data.get("product_description")
    return_reason = data.get("return_reason")

    image, return_reasons = defect_detect.detect_defects(
        product_description, product_title, return_reason, product_img
    )

    rawBytes = io.BytesIO()
    product_img.save(rawBytes, "JPEG")
    rawBytes.seek(0)
    img_base64 = base64.b64encode(rawBytes.read())

    if not return_reasons or not return_reasons[0].coordinates:
        return jsonify({"message": "No defects found!"}), 200
    else:
        return jsonify(
            {
                "defects": [
                    return_reason.description for return_reason in return_reasons
                ],
                "image": str(img_base64),
            }
        )


@app.route("/detect-size", methods=["POST"])
def defect_detection():
    data = request.json

    if "product_img" not in request.files:
        return jsonify({"error": "No file part"}), 400

    product_img = request.files["product_img"]
    if product_img.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    if "user_img" in request.files:
        user_img = request.files["user_img"]
    else:
        user_img = None
    
    product_title = data.get("product_title")
    product_description = data.get("product_description")
    return_reason = data.get("return_reason")

    return defect_detect.detect_defects(
        product_description, product_title, return_reason, product_img, user_img
    )


if __name__ == "__main__":
    app.run(debug=True, port=2000)
