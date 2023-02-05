from flask import Flask
from flask_restful import reqparse, Api, Resource
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')
class Message(Resource):
    def get(self):
        return {"message": 'Test'}
api.add_resource(Message, './pages/api/flask')

if __name__ == '__main__':
    app.run(debug=True)