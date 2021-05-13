import os
#import sys
import pickle
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import numpy as np
#from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)
CORS(app)
api = Api(app)
# Require a parser to parse our POST request.
parser = reqparse.RequestParser()
parser.add_argument("age")
parser.add_argument("sex")
parser.add_argument("cp")
parser.add_argument("trtbps")
parser.add_argument("chol")
parser.add_argument("fbs")
parser.add_argument("restecg")
parser.add_argument("thalachh")
parser.add_argument("exng")
parser.add_argument("oldpeak")
parser.add_argument("caa")
parser.add_argument("thall")
# Unpickle our model so we can use it!
if os.path.isfile("./test_model.pkl"):
  model = pickle.load(open("./test_model.pkl", "rb"))
else:
  raise FileNotFoundError
class Predict(Resource):
  def post(self):
    args = parser.parse_args()
# Sklearn is VERY PICKY on how you put your values in...
    X = (
      np.array(
        [
          args["age"],
          args["sex"],
          args["cp"],
          args["trtbps"],
          args["chol"],
          args["fbs"],
          args["restecg"],
          args["thalachh"],
          args["exng"],
          args["oldpeak"],
          args["caa"],
          args["thall"]
        ]
        ).astype("float").reshape(1, -1)
    )
    #normalize = MinMaxScaler()
    #X = normalize.fit_transform(X)

    _y = model.predict(X)[0].item()
    return {"class": _y}
api.add_resource(Predict, "/predict")
if __name__ == "__main__":
  app.run(debug=True)




















