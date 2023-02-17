# Import necessary modules
from api.v1.views import app_views
from flask import jsonify

# Define a route for the "/status" endpoint
@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})

from models import storage

# Define a route for the "/stats" endpoint
@app_views.route('/stats', methods=['GET'])
def get_stats():
    # Get a dictionary of class names and their corresponding count
    stats = {}
    for cls in storage.classes:
        count = storage.count(cls)
        stats[cls] = count

    # Return the dictionary as a JSON response
    return jsonify(stats)
