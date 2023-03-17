from facebook_scraper import *
from flask import Flask
from flask_restx import Api
from fbpages import api as pages  
from fbprofile import api as profile
from fbgroups import api as groups

app = Flask(__name__)
api = Api(app)


api.add_namespace(profile)
api.add_namespace(pages)
api.add_namespace(groups)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)




