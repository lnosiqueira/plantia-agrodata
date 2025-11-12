# API Python (Flask)
from flask import Flask, request, jsonify
import cx_Oracle

app = Flask(__name__)

@app.route('/api/sensores', methods=['POST'])
def receber_dados():
    dados = request.json
    conn = cx_Oracle.connect('usuario/senha@host:porta/servico')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sensores_agrodata (soil_moisture, rainfall, temperature, humidity) VALUES (:1, :2, :3, :4)",
                   (dados['soil_moisture'], dados['rainfall'], dados['temperature'], dados['humidity']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"status": "sucesso"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
