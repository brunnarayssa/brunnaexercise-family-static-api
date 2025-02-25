from flask import Flask, jsonify, request
from flask_cors import CORS
from src.datastructure import FamilyStructure  # Importación corregida

app = Flask(__name__)
CORS(app)

jackson_family = FamilyStructure('Jackson')

# Obtener todos los miembros
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Obtener un miembro específico
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# Agregar un nuevo miembro
@app.route('/member', methods=['POST'])
def add_member():
    data = request.get_json()
    if not data or not "first_name" in data or not "age" in data or not "lucky_numbers" in data:
        return jsonify({"error": "Invalid input"}), 400

    jackson_family.add_member(data)
    return jsonify({"msg": "Member added successfully"}), 200

# Eliminar un miembro
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    result = jackson_family.delete_member(member_id)
    if result:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
