from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')# теперь следующая функция откликается на url: /  как регвест мап в джавке

def home():
    return jsonify(message="hello, DevOps") 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)