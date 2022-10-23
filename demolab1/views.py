from flask import jsonify, request
from demolab1 import app


CATEG = [
    {
        "id": 1,
        "name": "Food"
    },
]


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEG})


@app.route("/category", methods=['POST'])
def create_category():
    request_data = request.get_json()
    CATEG.append(request_data)
    print(request_data)
    return jsonify(request_data)

