from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Listas de nombres y apellidos latinos
nombres_latinos = ["Carlos", "María", "José", "Ana", "Luis", "Paula", "Javier", "Gabriela", "Fernando", "Isabel"]
apellidos_latinos = ["González", "Rodríguez", "López", "Fernández", "Pérez", "Gómez", "Díaz", "Martínez", "Castillo", "Ramírez"]

# Dominios de correo
email_domains = ["gmail.com", "hotmail.com", "yahoo.com"]

# Calles reales de Ciudad de Panamá
calles_panama = [
    "Avenida Balboa", "Vía España", "Calle 50", "Vía Argentina", "Cinta Costera",
    "Avenida Justo Arosemena", "Vía Brasil", "Calle Uruguay", "Vía Porras", "Calle Samuel Lewis"
]

@app.route("/", methods=["GET", "POST"])
def index():
    telefono_ingresado = ""
    datos = None

    if request.method == "POST":
        telefono_ingresado = request.form.get("telefono")

        if telefono_ingresado and telefono_ingresado.isdigit() and len(telefono_ingresado) == 8 and telefono_ingresado[0] == "6":
            datos = generar_datos(telefono_ingresado)
        else:
            datos = {"error": "El número debe tener 8 cifras y comenzar con 6."}

    return render_template("index.html", telefono=telefono_ingresado, datos=datos)

def generar_datos(telefono):
    # Generar correo aleatorio
    email = f"user{random.randint(1000,9999)}@{random.choice(email_domains)}"

    # Generar nombres y teléfonos latinos
    nombre1 = f"{random.choice(nombres_latinos)} {random.choice(apellidos_latinos)}"
    telefono1 = f"6{random.randint(1000000, 9999999)}"

    nombre2 = f"{random.choice(nombres_latinos)} {random.choice(apellidos_latinos)}"
    telefono2 = f"6{random.randint(1000000, 9999999)}"

    # Generar una dirección real de Panamá
    direccion = f"{random.choice(calles_panama)} #{random.randint(1, 999)}, Ciudad de Panamá"

    return {
        "correo": email,
        "nombre1": nombre1,
        "telefono1": telefono1,
        "nombre2": nombre2,
        "telefono2": telefono2,
        "direccion": direccion
    }

if __name__ == "__main__":
    app.run(debug=True)
