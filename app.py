from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Como nosso teste unitário valida exatamente se a mensagem é a que estamos esperando, o teste unitário vai falhar por ter ficado com a mensagem antiga"
