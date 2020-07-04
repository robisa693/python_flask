#This is the main flask module
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	if (request.method == 'POST'):
		json_example = request.get_json()
		return jsonify({'You sent me': json_example}), 201
	else:
		return jsonify({"about" : "Hello World!"})

@app.route('/multiply/<int:num>', methods=['GET'])
def get_multiply100(num):
	return jsonify({'result': num*10})

if __name__ == "__main__":
	app.run(debug=True)

