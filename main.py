from flask import Flask, render_template, request, jsonify
import datetime
import json
import pymongo
from DataBase import DataBase

myDB = DataBase.DataBase

json_output = myDB.regresadic()
json_output = json.loads(json_output)


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", name_json=json_output)

@app.route('/dia-semana', methods=['POST'])
def obtener_dia_semana():
    data = request.get_json()
    fecha_str = data.get('fecha')
    try:
        fecha = datetime.datetime.strptime(fecha_str, '%d/%m/%Y')
        dia_semana = fecha.strftime('%A')
        return jsonify({'fecha': fecha_str, 'dia_semana': dia_semana})
    except ValueError:
        return jsonify({'error': 'La fecha debe estar en formato DD/MM/AAAA'})
    
@app.route('/usuario', methods=['POST'])
def obtener_Usuario():
    data = request.get_data(as_text=True)
    res = json.loads(data)
    
    try:
        
        
        json_output = myDB.regresaUser(res["User"])

        return jsonify(json_output)   
    except ValueError:
        return jsonify({'error': request.get_data()})
    

    

if __name__ == '__main__':
    app.run()