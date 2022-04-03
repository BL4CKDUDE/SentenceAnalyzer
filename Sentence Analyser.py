from flask import Flask, request, jsonify, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/test', methods=["GET","POST"])
def list_post():
    json_body = request.get_json()
    q = json_body['question']
    return q

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)