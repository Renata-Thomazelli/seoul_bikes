# App Web to preview the quantity of bikes
# app flask

# Imprts
import sys
sys.path.append('D:\Projetos\ML\Seoul_bikes')

from flask import Flask, request
from flask import render_template
from tools.bike import Bikes

# Cria a app
app = Flask(__name__)

# Página de entrada
@app.route("/")
def index():
    result = None
    return render_template("index.html", result = result)

# Página com resultado da previsão
@app.route("/estimate", methods = ["POST"])
def estimate():
    values = request.form.getlist('new_bikes_estimative')
    bike = Bikes(values)
    value_to_predict = bike.prepare()
    result = bike.predict(value_to_predict)
    result = "%.2f" % result
    return render_template('index.html', result = result)

# Executa a app
if __name__ == "__main__":
    app.run(host = 'localhost', port = 3000, debug = True)