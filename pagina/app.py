from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def registrar_log(accion):
    with open("backup.log", "a") as f:
        f.write(f"[{datetime.datetime.now()}] {accion}\n")

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        try:
            if tipo == 'logica':
                v1 = bool(int(request.form['v1']))
                v2 = bool(int(request.form['v2']))
                op = request.form['op']
                resultado = v1 and v2 if op == 'AND' else v1 or v2
                registrar_log(f"Calculadora Lógica: {v1} {op} {v2} = {resultado}")
            # Aquí puedes añadir las ramas para aritmética y binaria
        except Exception as e:
            resultado = f"Error: {e}"
    return render_template('pagina.html', resultado=resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)