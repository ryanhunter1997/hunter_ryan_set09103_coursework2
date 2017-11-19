from flask import Flask, render_template
app = Flask(__name__,)

@app.route('/')
def splash():
    return render_template('splash.html'), 200

@app.route('/home')
def home():
    return render_template('home.html'), 200

@app.route('/listen')
def listen():
    return render_template('listen.html'),200

@app.route('/listen/concreteandgold')
def candg():
    return render_template('candg.html'), 200
@app.route('/listen/sonichighways')
def sonic():
    return render_template('sonic.html'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
