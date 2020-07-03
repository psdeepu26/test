from http_server_mock import HttpServerMock
import requests

class Test_MainProgram(unittest.TestCase):
    def test_http_server_mock(self):
        print("------------------ Test Case : HTTP Server Mock ------------------")
        app = HttpServerMock(__name__, is_alive_route="/metrics")

        @app.route("/", methods=["GET"])
        def index():
            return "Prometheus Metrics"

        with app.run("localhost", 8000):
            r = requests.get("http://localhost:8000/")
        print("------------------------ Test Case : Completed ------------------\n")

if __name__ == '__main__':
    unittest.main()
