from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    data = request.json
    print("Yeni canlı skor verisi geldi:")
    print(data)

    with open("live_scores.json", "a") as f:
        json.dump(data, f, ensure_ascii=False)
        f.write("\n")

    return jsonify({"status": "success"}), 200

@app.route('/scores', methods=['GET'])
def scores():
    scores = []
    try:
        with open("live_scores.json", "r") as f:
            for line in f:
                scores.append(json.loads(line))
    except FileNotFoundError:
        pass
    return jsonify(scores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
