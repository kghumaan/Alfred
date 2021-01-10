from flask import Flask, render_template
from flask_restplus import Api, Resource
import socket

from resources.recipe_generator import RecipeGenerator

app = Flask(__name__)
api = Api(app=app)

""" Home page - currently just prints the host and IP of the client """
@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')

""" Mounting all of our resources, these are the entry points for our API """
api.add_resource(RecipeGenerator, '/api/recipe/')

# TODO: eventually iterate over the files under /resources, instead of mounting explicitly

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
