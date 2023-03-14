import socket
from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template(template_name_or_list='index.html')


@app.route('/send/', methods=['GET'])
def send():
    # Connect to remote server
    HOST = 'localhost'
    PORT = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, server!')
        data = s.recv(1024)
        print(data)
        return data

if __name__ == '__main__':
    app.run()
