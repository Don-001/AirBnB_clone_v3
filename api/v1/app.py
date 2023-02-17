# Import necessary modules
from flask import Flask
from api.v1.views import app_views
from models import storage

# Create the Flask application instance
app = Flask(__name__)

# Register the app_views blueprint to the app
app.register_blueprint(app_views, url_prefix='/api/v1')

# Define a method to handle the teardown_appcontext event
@app.teardown_appcontext
def close_storage(error):
    storage.close()

# Run the Flask application if this file is executed
if __name__ == '__main__':
    # Set the default values for host and port
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))

    # Run the Flask application
    app.run(host=host, port=port, threaded=True)
