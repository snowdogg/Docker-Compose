import redis
from flask import Flask

app = Flask(__name__)
counter = redis.Redis(host='redis', port=6379)

@app.route("/")
def home():
	counter.incr('hits')
	return "This is a fantastic web app, and it is powered by Flask. \nIt has been viewed %d time(s)." % int(counter.get('hits'))

if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0')
