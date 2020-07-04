#This is using the flask restful submodule

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		return {"about" : "Hello World!"}
	def post(self):
		your_data = request.get_json()
		if your_data == None:
			your_data = "empty"
		return {'You sent me': your_data}, 201


class Multi(Resource):
	def get(self, num):
		return {'result': num*100}

api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multiply/<int:num>')		

if __name__ == "__main__":
	app.run(debug=True)

