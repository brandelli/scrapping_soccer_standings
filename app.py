from flask import Flask
from flask_restful import Api

from resources.todo import Todo, Todos
from resources.soccer import Leagues, League, Standing

app = Flask(__name__)
api = Api(app)

api.add_resource(Todo, "/todo/<int:id>")
api.add_resource(Todos, "/todo/")

api.add_resource(Leagues, "/leagues/")
api.add_resource(League, "/leagues/<int:id>")
api.add_resource(Standing, "/standing/<int:id>")


if __name__ == "__main__":
  app.run(debug=True)