#!/usr/bin/python3
"""import app flask jsonify"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os
"""
flask
"""


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """
    teardown app context
    """
    storage.close()


if __name__ == '__main__':
    """
    main
    """
    host = '0.0.0.0'
    port = 5000
    if os.getenv('HBNB_API_HOST'):
        host = os.getenv('HBNB_API_HOST')
    if os.getenv('HBNB_API_PORT'):
        port = os.getenv('HBNB_API_PORT')
    app.run(host=host, port=port, threaded=True)
