# A simple web server that serves a static HTML file.
# This script uses Python's built-in http.server module, so no external libraries are needed.

## import http.server
## import socketserver

# Set the port for the server to run on.
## PORT = 8000

# Create a handler to serve files from the current directory.
# The SimpleHTTPRequestHandler is a built-in class for this purpose.
## Handler = http.server.SimpleHTTPRequestHandler

# Start the server. The with statement ensures the server is properly closed.
## with socketserver.TCPServer(("", PORT), Handler) as httpd:
    ## print(f"Serving web app at http://localhost:{PORT}")
    
    # Run the server indefinitely until it is manually stopped.
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping the server...")
