from flask import Flask  # Imports Flask, a framework for creating web applications simply and quickly.

from threading import Thread  # Imports Thread from threading to run functions in parallel without blocking program execution.

# Initializes an instance of the Flask application.
# Flask takes the current module name as an argument, which in this case is an empty string ('').
# This allows Flask to locate files and resources related to the application.
app = Flask('')

# Defines the root route of the web application.
# @app.route('/') is a decorator that specifies that the `home` function will be executed
# when the root URL (/) of the server is accessed. This sets up an access point to the application.
@app.route('/')
def home():
    # The `home` function responds with the text "I'm alive" when the root URL is requested.
    # This indicates that the server is running correctly.
    return "I'm alive"

# Defines a `run` function that will start the Flask server when called.
# This function configures the server to be publicly accessible on the network.
def run():
    # `app.run` starts the Flask server with the following configurations:
    # - host='0.0.0.0' allows public access to the server on the network, ideal for applications that need external monitoring.
    # - port=8080 sets the port on which the server will listen for incoming requests.
    app.run(host='0.0.0.0', port=8080)

# Defines a `keep_alive` function that keeps the web server running in the background.
# This is useful for bots or services that need a continuously running server without blocking the main program flow.
def keep_alive():
    # Creates and starts a new thread that will run the `run` function independently.
    # `Thread(target=run)` creates a thread that will run the `run` function.
    # `t.start()` starts the thread, running the Flask server in the background.
    t = Thread(target=run)
    t.start()
