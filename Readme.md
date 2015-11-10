Flask-Sse
=========

A simple [Flask][0] extension for HTML5 [server-sent events][1] support, powered by [Redis][2]

The extension provides 2 things - a blueprint with a single route for streaming events, and a helper function to send messages to subscribers:

    from flask import Flask, json
    from flask.ext.sse import sse, send_event
    
    app = Flask(__name__)
    app.register_blueprint(sse, url_prefix='/stream')
    
    @app.route('/send')
    def send_message():
        send_event('myevent', json.dumps({"message": "Hello!"}))
        
You can then subscribe to these events in a supported browser:

    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8" />
    </head>
    <body>
      <script>
        var source = new EventSource("{{ url_for('sse.stream') }}");
        source.addEventListener('myevent', function(e) {
            var data = JSON.parse(e.data);
            // handle event
        }, false);
      </script>
    </body>
    </html>

The source comes with a basic example

Clients can subscribe to different channels by setting 'channel' on the query string, which defaults to 'sse'. These correspond to redis channels.

    def send_message():
        send_event('myevent', json.dumps({"line": "Something happened"}), channel='logs')
    
    #######
        
    var source = new EventSource("{{ url_for('sse.stream', channel='logs') }}")    
    
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

Subscribers will connect and block for a long time, so you should seriously consider running under an asynchronous WSGI server, such as gunicorn+gevent (like the example)

I should also say I'm not really maintaining this beyond accepting the odd pull request - it was built as an experiment but I'm not using it in anger on anything production. I wont be publishing it on PyPi myself for the same reasons - if I start using it properly then it will go on PyPi and have some tests put around it.

Credits
=======
Inspired by [django-sse](https://github.com/niwibe/django-sse)


[0]:http://flask.pocoo.org
[1]:http://en.wikipedia.org/wiki/Server-sent_events
[2]:http://redis.io/
