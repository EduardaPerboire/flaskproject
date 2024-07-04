from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/motion-detected', methods=['POST'])
def motion_detected():
    data = request.json
    print('Motion detected data received:', data)

    return jsonify({"status": "success", "message": "Data received"}), 200

if __name__ == '__main__':
    print("executando...")
    app.run(host='0.0.0.0', port=5000)
