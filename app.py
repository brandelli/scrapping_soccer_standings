import os
import pymongo
from flask import Flask
from flask_restful import Api
from flask_cors import CORS


from resources.soccer import Leagues, League, Standing

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Leagues, "/leagues/")
api.add_resource(League, "/leagues/<int:id>")
api.add_resource(Standing, "/standing/<int:id>")


if __name__ == "__main__":
  app.run(debug=True)