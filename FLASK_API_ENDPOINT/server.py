from flask import Flask

app = Flask(__name__)

# send json
@app.route('/hello_json')
def helloJson():
    return {'message': 'Hello World!!!'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50100, debug=True)