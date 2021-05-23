import os
import sys
#import pickle
from  xgboost import XGBRFClassifier
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
parser.add_argument("sex")
parser.add_argument("cp")
parser.add_argument("fbs")
parser.add_argument("restecg")
parser.add_argument("exng")
parser.add_argument("oldpeak")
parser.add_argument("slp")
parser.add_argument("caa")
# load our model so we can use it!
if os.path.isfile("./final_model"):
    model = XGBRFClassifier()
    model.load_model("final_model")
else:
  raise FileNotFoundError
class Predict(Resource):
  def post(self):
    args = parser.parse_args()

    X = (
      np.array(
        [
          args["sex"],
          args["cp"],
          args["fbs"],
          args["restecg"],
          args["exng"],
          args["oldpeak"],
          args["slp"],
          args["caa"],
        ]
        ).astype("float").reshape(1, -1)
    )

    print(model.predict(X)[0], file=sys.stderr)  
    _y = model.predict(X)[0].item()
    return {"class": _y}
api.add_resource(Predict, "/predict")
if __name__ == "__main__":
  app.run(debug=True)





















