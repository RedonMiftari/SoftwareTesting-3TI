from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/') #i.p.v. / een url moet ingevuld worden als route waar deze geopened kan worden.

def home():
    return jsonify({'message': 'Hello, world!'})

if __name__ == '__main__':
    app.run()