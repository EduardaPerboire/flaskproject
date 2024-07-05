from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/motion-detected', methods=['POST'])
def motion_detected():
    try:
        # Logando os cabeçalhos da requisição
        print("Headers received:", request.headers)

        # Tentando obter dados JSON
        data = request.get_json(silent=True)
        if data:
            print("Webhook received JSON data:", data)
            return jsonify({"status": "success", "message": "JSON data received"}), 200
        else:
            # Se não for JSON, tente obter dados brutos (texto ou outros formatos)
            raw_data = request.data
            print("Webhook received raw data:", raw_data.decode('utf-8'))
            return jsonify({"status": "success", "message": "Raw data received"}), 200
        
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    print("executando...")
    app.run(host='0.0.0.0', port=5000)
