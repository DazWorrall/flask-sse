Flask-Sse
=========

A simple [Flask][0] extension for HTML5 [server-sent events][1] support, powered by [Redis][2]

The extension provides 2 things - a blueprint with a single route, for streaming events, and a helper function to send messages to subscribers:

    from flask import Flask, json
    from flask.ext.see import sse, send_event
    
    app = Flask(__name__)
    app.register_blueprint(sse, url_prefix='/stream')
    
    @app.route('/send')
    def send_message()
        send_event('myevent', json.dumps({"message": "Hello!"}))
        
You can then subscribe to these events in a supported browser:

        var source = new EventSource("/stream");
        source.addEventListener('testevent', function(e) {
            var data = JSON.parse(e.data);
            document.body.innerHTML += "New Message: " + data.message + '<br />';
        }, false);

The source comes with a basic example

Clients can subscribe to different channels by setting 'channel' on the query string, which defaults to 'sse'. These correspond to redis channels.

    def send_message()
        send_event('myevent', json.dumps({"line": "Something happened"}), channel='logs')
    
    #######
        
    var source = new EventSource("/stream?channel=logs")    
    
Being a blueprint, you can attach a before_request handler to handle things like access control:


    @sse.before_request
    def check_access():
        if request.args.get('channel') == 'firehose' and not g.user.is_admin():
            abort(403)



Configuration
=============

Redis connection details are read from the applications config using the following keys (defaults in [])

* SSE_REDIS_HOST [localhost]
* SSE_REDIS_PORT [6379]
* SSE_REDIS_DB \[0\]


Caveats
=======

Subscribers will connect and block for a long time, so you should seriously consider running under an asyncronous WSGI server, such as gunicorn+gevent (like the example)


[0]:http://flask.pocoo.org
[1]:http://en.wikipedia.org/wiki/Server-sent_events
[2]:http://redis.io/