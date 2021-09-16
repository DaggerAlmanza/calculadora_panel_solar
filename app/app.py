from flask import Flask, request, jsonify
from core.models import HomeAppliance

app = Flask(__name__)


@app.route('/electrodomesticos', methods=['POST'])
def electrodomesticos():
    data = request.get_json()
    iron = HomeAppliance(**data["homeAppliaces"][0])
    
    return jsonify({'datos': data})
