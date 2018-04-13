Flask
=====

Flask is a very lightweight `WSGI` web application framework. It is designed to make getting started quick and easy,
 with the ability to scale up to complex applications. It began as a simple wrapper around `Werkzeug` and `Jinja` 
 and has become one of the most popular Python web application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or project layout. It is up to the developer to choose
 the tools and libraries they want to use. There are many extensions provided by the community that make adding new 
 functionality easy.

This repository is for Docker build by Dockerfile.

Installing
----------

Install and update using `pip`:

    pip install -U Flask

A Simple Example
----------------

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Flask Image For Python:3.6.5-alpine'
        
Log:            
            
    * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

Docker Container
----------------

Launching the flask app via docker container,the port 5000(by default) should bind to specific port.

Links
----------------
 
Docker Hub: <https://hub.docker.com/r/aeoluswing/flask/>  
Wsgi: <https://wsgi.readthedocs.io>  
Werkzeug: <http://werkzeug.pocoo.org/>  
Jinja: <http://jinja.pocoo.org/>  
Pip: <https://pip.pypa.io/en/stable/quickstart/>  

     