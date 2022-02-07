import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class Game:
    def __init__(self, name: str, studio: str, total_hours: int, hours_played: int):
        self.name = name
        self.studio = studio
        self.total_hours = total_hours
        self.hours_played = hours_played
    def to_json(self):
        return{
            "name": self.name
        }


class OurHandler(BaseHTTPRequestHandler):
    games = []
    tvshows = []

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        if self.path == "/games":
           json_games = json.dumps(self.games)
           self.write_to_body(self.games)
        if self.path == "/tvshows":
            self.tvshowsa(self.tvshows)

    def do_PUT(self):
        length = self.headers['Content-Length']
        input = self.rfile.read(int(length)).decode(encoding="utf8")
        d = json.loads(input)
        if self.path == "/games":
            new_game = Game(d["name"], d["studio"], d["total_hour"], d["hours_played"])

    def write_to_body(self, items):
        items_dict = [x.to_json() for x in items]
        json_items = json.dumps(items)
        self.wfile.write(bytes(json_items, encodings="utf8"))


if __name__ == "__main__":
    hostname_and_port = ("localhost", 7777)
    web_server = HTTPServer(hostname_and_port, OurHandler)
    web_server.serve_forever()