from flask import Flask
import debugpy

app = Flask(__name__)


@app.route("/")
def helloworld():
    """Return a hello world greeting on endpoint /"""
    message = "Hello World"
    return message


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    debugpy.listen("0.0.0.0", 5678)
    debugpy.wait_for_client()
