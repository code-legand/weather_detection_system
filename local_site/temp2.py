import socket
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to remote server
    HOST = 'localhost'
    PORT = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, server!')
        data = s.recv(1024)
        print(data)

    return render_template('index.html', data=data.decode())

if __name__ == '__main__':
    app.run()
