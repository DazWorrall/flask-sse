from flask import Flask, render_template, redirect, url_for, json, request

try:
    from flask.ext.sse import sse, send_event
except ImportError:
    import sys
    sys.path.append('..')
    from flask.ext.sse import sse, send_event

app = Flask(__name__)
app.debug = True
app.register_blueprint(sse, url_prefix='/events')

@app.route('/new')
def new():
    return render_template('message.html')

@app.route('/send', methods=['POST'])
def send():
    data = {"message": request.form.get('message', 'Hello, world!')}
    send_event("testevent", json.dumps(data), channel='test')
    return redirect(url_for('new'))

@app.route('/')
def index():
    return render_template('index.html')
