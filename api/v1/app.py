#!/usr/bin/python3
"""
import app flask jsonify
"""


from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from models import storage
from flask_cors import CORS
import os
"""
flask
"""


app = Flask(__name__)
app.register_blueprint(app_views)


cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(exception):
    """
    teardown app context
    """
    storage.close()


@app.errorhandler(404)
def error(error):
    """
    error not found
    """
    return (jsonify({"error": "Not found"}), 404)


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
