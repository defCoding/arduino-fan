from flask import Flask, send_from_directory, request, redirect, url_for
import arduino

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/btn', methods=['POST'])
def btn_press():
    state = int(request.form['state'])
    print(state)
    arduino.send_byte(state)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
