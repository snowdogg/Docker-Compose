import redis
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "This is a fantastic web app, and it is powered by Flask."

if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0')