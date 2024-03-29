from flask import Flask
from src.routes.routes import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TADSBINCALC'


app.add_url_rule(routes["index_route"], view_func= routes["index_route_controller"])
app.add_url_rule(routes["binarioSM_route"], view_func= routes["binarioSM_route_controller"])
app.add_url_rule(routes["binarioCTWO_route"], view_func= routes["binarioCTWO_route_controller"])
app.add_url_rule(routes["decimalBinary_route"], view_func= routes["decimalBinary_route_controller"])