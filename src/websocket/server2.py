from flask import Flask 
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'
socketio = SocketIO(app)


@app.route('/')
def index():
    return '测试成功'






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)




















