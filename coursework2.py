from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def splash():
    return render_template('splash.html'), 200

@app.route('/home')
def home():
    return render_template('home.html'), 200

@app.route('/listen')
def listen():
    return render_template('listen.html'),200

@app.route('/watch')
def watch():
    return render_template('watch.html'), 200

@app.route('/listen/concreteandgold')
def candg():
    return render_template('candg.html'), 200

@app.route('/listen/sonichighways')
def sonic():
    return render_template('sonic.html'), 200

@app.route('/listen/wastinglight')
def wasting():
    return render_template('wasting.html'), 200

@app.route('/listen/greatesthits')
def greatest():
    return render_template('greatest.html')

@app.route('/listen/espg')
def echoes():
    return render_template('echoes.html'), 200

@app.route('/listen/inyourhonor')
def honor():
    return render_template('honor.html'), 200

@app.route('/listen/onebyone')
def one():
    return render_template('one.html'), 200

@app.route('/listen/tnltl')
def nothing():
    return render_template('nothing.html'), 200

@app.route('/listen/tcats')
def tcats():
    return render_template('tcats.html'), 200

@app.route('/listen/foofighters')
def foo():
    return render_template('foo.html'), 200

@app.route('/watch/sky')
def sky():
    return render_template('sky.html'), 200

@app.route('/watch/run')
def run():
    return render_template('run.html'), 200

@app.route('/watch/pretender')
def pre():
    return render_template('pretender.html'), 200

@app.route('/watch/everlong')
def ever():
    return render_template('everlong.html'), 200

@app.route('/watch/learntofly')
def fly():
    return render_template('learntofly.html'), 200

@app.route('/watch/allmylife')
def life():
    return render_template('allmylife.html'), 200


@app.route('/watch/somethingfromnothing')
def something():
    return render_template('somethingfromnothing.html'), 200

@app.route('/watch/congregation')
def congregation():
    return render_template('congregation.html'), 200

@app.route('/watch/timeslikethese')
def times():
    return render_template('timeslikethese.html'), 200

@app.route('/watch/walk')
def walk():
    return render_template('walk.html'),200

@app.route('/events')
def events():
    return render_template('events.html'),200

@app.route('/social')
def social():
    return render_template('social.html'),200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
