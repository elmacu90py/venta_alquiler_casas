import casas
from flask import Flask, render_template
app = Flask(__name__) # Instancia la clase flask y crea el objeto app

@app.route('/') # este es el index

def indice():
    datos = casas.casas() # esto devuelve los datos escrapeados
    return render_template('index.html', datos=datos)

if __name__ == "__main__":
    app.run()

