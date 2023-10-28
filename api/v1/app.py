#!/usr/bin/python3
"""
import app flask jsonify
"""


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


@app.errorhandler(404)
def error(error):
    """
    error not found
    """
    return (jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', 5000)
    
    app.run(host=host, port=port, threaded=True)
