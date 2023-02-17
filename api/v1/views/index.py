# Import necessary modules
from api.v1.views import app_views
from flask import jsonify

# Define a route for the "/status" endpoint
@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})
