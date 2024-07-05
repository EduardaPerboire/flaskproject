from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/motion-detected', methods=['POST'])
def motion_detected():
    try:
        data = request.get_json(silent=True)
        if data:
            print("Webhook received JSON data:", data)
            print('Motion detected data received:', data)
            return jsonify({"status": "success", "message": "Data received"}), 200
        else:
            # Se não for JSON, tente obter dados brutos (texto ou outros formatos)
            data = request.data
            print("Webhook received raw data:", data)
            return jsonify({"status": "error", "message": str(e)}), 400
        
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"status": "error", "message": str(e)}), 412

if __name__ == '__main__':
    print("executando...")
    app.run(host='0.0.0.0', port=5000)
