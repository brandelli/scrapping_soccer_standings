from flask import Flask
from flask_restful import Api

from resources.todo import Todo, Todos

app = Flask(__name__)
api = Api(app)

api.add_resource(Todo, "/todo/<int:id>")
api.add_resource(Todos, "/todo/")


if __name__ == "__main__":
  app.run(debug=True)