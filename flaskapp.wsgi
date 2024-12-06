import sys
import logging

# Adjust the path to your application directory
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/myapp/hello-world")  # Ensure this matches your app's directory

from app import app as application  # Import the Flask app instance from app.py
