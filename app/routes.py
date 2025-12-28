from flask import Blueprint, request, jsonify
from .logic.cyk import cyk_parse 

parser_bp = Blueprint('parser', __name__)

@parser_bp.route("/parse", methods=["POST"])
def parse():
    data = request.get_json()
    
    if not data or "sentence" not in data:
        return jsonify({"error": "No sentence provided"}), 400
        
    sentence = data["sentence"]
    accepted, table, words = cyk_parse(sentence)

    table_json = [[list(cell) for cell in row] for row in table]

    return jsonify({
        "accepted": accepted,
        "words": words,
        "table": table_json
    })