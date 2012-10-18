#!/bin/bash
gunicorn -k gevent -b 0.0.0.0:5000 --debug example:app
