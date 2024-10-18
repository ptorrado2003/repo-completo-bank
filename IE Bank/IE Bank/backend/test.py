import pytest
from your_app import app, db
from your_app.models import Cuenta

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    db.create_all()
    yield app.test_client()
    db.session.remove()
    db.drop_all()

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Bienvenido a la API de cuentas"

def test_create_account(client):
    data = {"nombre": "Juan", "email": "juan@example.com"}
    response = client.post("/accounts", json=data)
    assert response.status_code == 200
    assert response.json["mensaje"] == "Cuenta creada con éxito!"
    cuenta = Cuenta.query.get(1)
    assert cuenta.nombre == "Juan"
    assert cuenta.email == "juan@example.com"

def test_create_account_sin_nombre(client):
    data = {"email": "juan@example.com"}
    response = client.post("/accounts", json=data)
    assert response.status_code == 400
    assert response.json["mensaje"] == "Faltan datos"

def test_create_account_con_email_existente(client):
    data = {"nombre": "Juan", "email": "juan@example.com"}
    client.post("/accounts", json=data)
    response = client.post("/accounts", json=data)
    assert response.status_code == 400
    assert response.json["mensaje"] == "Correo electrónico ya existe"

def test_get_accounts(client):
    cuenta1 = Cuenta(nombre="Juan", email="juan@example.com")
    cuenta2 = Cuenta(nombre="Maria", email="maria@example.com")
    db.session.add_all([cuenta1, cuenta2])
    db.session.commit()
    response = client.get("/accounts")
    assert response.status_code == 200
    assert len(response.json["cuentas"]) == 2
    assert response.json["cuentas"][0]["nombre"] == "Juan"
    assert response.json["cuentas"][1]["nombre"] == "Maria"

def test_get_account_by_id(client):
    cuenta = Cuenta(nombre="Juan", email="juan@example.com")
    db.session.add(cuenta)
    db.session.commit()
    response = client.get(f"/accounts/{cuenta.id}")
    assert response.status_code == 200
    assert response.json["cuenta"]["nombre"] == "Juan"

def test_get_account_by_id_no_encontrada(client):
    response = client.get("/accounts/1")
    assert response.status_code == 404
    assert response.json["mensaje"] == "Cuenta no encontrada"

def test_update_account_by_id(client):
    cuenta = Cuenta(nombre="Juan", email="juan@example.com")
    db.session.add(cuenta)
    db.session.commit()
    data = {"nombre": "Juanito"}
    response = client.put(f"/accounts/{cuenta.id}", json=data)
    assert response.status_code == 200
    assert response.json["mensaje"] == "Cuenta actualizada con éxito!"
    cuenta_actualizada = Cuenta.query.get(cuenta.id)
    assert cuenta_actualizada.nombre == "Juanito"

def test_delete_account(client):
    cuenta = Cuenta(nombre="Juan", email="juan@example.com")
    db.session.add(cuenta)
    db.session.commit()
    response = client.delete(f"/accounts/{cuenta.id}")
    assert response.status_code == 200
    assert response.json["mensaje"] == "Cuenta eliminada con éxito!"
    cuenta_eliminada = Cuenta.query.get(cuenta.id)
    assert cuenta_eliminada is None
