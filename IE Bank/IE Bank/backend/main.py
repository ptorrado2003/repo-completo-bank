import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

class Cuenta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    saldo = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"Cuenta('{self.nombre}', '{self.email}', '{self.saldo}')"

@app.route("/")
def root():
    return "Bienvenido a la API de cuentas"

@app.route("/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    if 'nombre' not in data or 'email' not in data:
        return jsonify({'mensaje': 'Faltan datos'}), 400
    if Cuenta.query.filter_by(email=data['email']).first():
        return jsonify({'mensaje': 'Correo electrónico ya existe'}), 400
    new_cuenta = Cuenta(nombre=data['nombre'], email=data['email'])
    db.session.add(new_cuenta)
    db.session.commit()
    return jsonify({'mensaje': 'Cuenta creada con éxito!'})

@app.route("/accounts", methods=['GET'])
def get_accounts():
    cuentas = Cuenta.query.all()
    output = []
    for cuenta in cuentas:
        cuenta_data = {'id': cuenta.id, 'nombre': cuenta.nombre, 'email': cuenta.email, 'saldo': cuenta.saldo}
        output.append(cuenta_data)
    return jsonify({'cuentas': output})

@app.route("/accounts/<account_id>", methods=['GET'])
def get_account_by_id(account_id):
    cuenta = Cuenta.query.get(account_id)
    if cuenta is None:
        return jsonify({'mensaje': 'Cuenta no encontrada'}), 404
    cuenta_data = {'id': cuenta.id, 'nombre': cuenta.nombre, 'email': cuenta.email, 'saldo': cuenta.saldo}
    return jsonify({'cuenta': cuenta_data})

@app.route("/accounts/<account_id>", methods=['PUT'])
def update_account_by_id(account_id):
    cuenta = Cuenta.query.get(account_id)
    if cuenta is None:
        return jsonify({'mensaje': 'Cuenta no encontrada'}), 404
    data = request.get_json()
    if 'nombre' in data:
        cuenta.nombre = data['nombre']
    if 'email' in data:
        if Cuenta.query.filter_by(email=data['email']).first():
            return jsonify({'mensaje': 'Correo electrónico ya existe'}), 400
        cuenta.email = data['email']
    if 'saldo' in data:
        cuenta.saldo = data['saldo']
    db.session.commit()
    return jsonify({'mensaje': 'Cuenta actualizada con éxito!'})

@app.route("/accounts/<account_id>", methods=['DELETE'])
def delete_account(account_id):
    cuenta = Cuenta.query.get(account_id)
    if cuenta is None:
        return jsonify({'mensaje': 'Cuenta no encontrada'}), 404
    db.session.delete(cuenta)
    db.session.commit()
    return jsonify({'mensaje': 'Cuenta eliminada con éxito!'})

if __name__ == "__main__":
    app.run(debug=True)
