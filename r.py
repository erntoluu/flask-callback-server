from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    data = request.json
    print("Yeni canlı skor verisi geldi:")
    print(data)
    # İstersen veriyi dosyaya kaydet
    with open("live_scores.json", "a") as f:
        f.write(str(data) + "\n")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
