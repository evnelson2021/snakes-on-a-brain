# This module will import json, http.server, and all necessary views containing the functions needed for doGET and doPOST
# This module will hold the HandleRequests class with doGET and doPOST functionality as well as the parse_url function that splits the url/path

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_species, get_single_species, get_all_snakes, get_single_snake, create_snake, get_all_owners, get_single_owner


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/species/1", the resulting list will
        # have "" at index 0, "species" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None
        if resource != "snakes" and resource != "owners" and resource != "species":
            self._set_headers(404)

        else:
            # Try to get the item at index 2
            try:
                # Convert the string "1" to the integer 1
                # This is the new parseInt()
                id = int(path_params[2])
            except IndexError:
                # self._set_headers(404)
                pass  # No route parameter exists: /species
            except ValueError:
                # self._set_headers(404)
                pass  # Request had trailing slash: /species/
            return (resource, id)  # This is a tuple
        # else:
        #     self._set_headers(404)

    def do_GET(self):
        """Handles GET requests to the server """
        response = {}

        # if response == {}:
        (resource, id) = self.parse_url(self.path)

        if resource == "species":
            if id is not None:
                response = get_single_species(id)
                if response == "Invalid request":
                    self._set_headers(404)
                else:
                    self._set_headers(200)

            else:
                response = get_all_species()
                self._set_headers(200)

        if resource == "snakes":
            if id is not None:
                response = get_single_snake(id)
                # checking value of response
                if response == "":
                    self._set_headers(405)
                elif response == "Invalid request":
                    self._set_headers(404)
                else:
                    self._set_headers(200)
            else:
                response = get_all_snakes()
                self._set_headers(200)

        if resource == "owners":
            if id is not None:
                response = get_single_owner(id)
                if response == "Invalid request":
                    self._set_headers(404)
                else:
                    self._set_headers(200)

            else:
                response = get_all_owners()
                self._set_headers(200)

        self.wfile.write(json.dumps(response).encode())

        # else:
        #     self._set_headers(404)


    def do_POST(self):
        """Handles POST requests to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new snake
        new_response = None

        # Add a new snake to the list.
        if resource == "snakes":
            new_response = create_snake(post_body)

        # Encode the new snake and send in response
        self.wfile.write(json.dumps(new_response).encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods','GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers','X-Requested-With, Content-Type, Accept')
        self.end_headers()


# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
