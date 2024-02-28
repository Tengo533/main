from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the HTTP request handler class

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Handler for GET requests
    def do_GET(self):
        self.send_response(200)

        # Send headers 
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Get the path from request
        path = self. path

        # Serve different pages based on the path
        if path == "/":
            # Serve main menu page
            html_content= """
            <html>
            <head>
                <title>Simple Web Server</title>
            </head>
            <body>
                <h1>Main Menu</h1>
                <form method="post" action="/page1">
                    <input type="submit" value="Open Page 1">
                </form>
                <form method="post" action="/page2">
                    <input type="submit" value="Open Page 2">
                </form>
            </body>
            </html>
            """
        elif path == "/page1":
            # Serve page 1
            html_content = """
            <html>
            <head>
                <title>Page 1</title>
            </head>
            <body>
                <h1>Page 1</h1>
                <p>This is Page 1 content.</p>
                <form method="post" action="/">
                    <input type="submit" value="Back to Main Menu">
                </form>
            </body>
            </html>
            """
        elif path == "/page2":
            # Serve page 2
            html_content = """
            <html>
            <head>
                <title>Page 2</title>
            </head>
            <body>
                <h1>Page 2</h1>
                <p>This is Page 2 content.</p>
                <form method="post" action="/">
                    <input type="submit" value="Back to Main Menu">
                </form>
            </body>
            </html>
            """
        else:
            # Handle invalid requests
            html_content = "<html><body><h1>404 Not Found</h1></body></html>"
        
        # Send the HTML content as response
        self.wfile.write(html_content.encode("utf-8"))

    #handler for POST requests (button clicks)
    def do_POST(self):
        # Send response status code
        self.send_response(303) # Redirect status code

        # Get the path from request

        path = self.path

        # Set the location heder to redirect to the respective pages
        if path == "/page1":
            self.send_header("Location", "/page1")
        elif path == "/page2":
            self.send_header("Location", "/page2")
        else:
            # Redirect to the main menu
            self.send_header("Location", "/")
        
        self.end_headers()

# Define the server parameters
host = "localhost"
port = 8000

# Create an HTTP server instance

server = HTTPServer((host,port), SimpleHTTPRequestHandler)

# Start the server
print(f"Server started at http://{host}:{port}")
server.serve_forever()