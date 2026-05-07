from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

@app.route("/galeria")
def galeria():
    return render_template("galeria.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)