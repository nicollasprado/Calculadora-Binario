from flask import Flask
from src.routes.routes import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TADSBINCALC'


app.add_url_rule(routes["index_route"], view_func= routes["index_route_controller"])
app.add_url_rule(routes["binarioSM_route"], view_func= routes["binarioSM_route_controller"])
app.add_url_rule(routes["binarioCTWO_route"], view_func= routes["binarioCTWO_route_controller"])
app.add_url_rule(routes["decimalBinary_route"], view_func= routes["decimalBinary_route_controller"])
app.add_url_rule(routes["decimalBinaryCTWO_route"], view_func= routes["decimalBinaryCTWO_route_controller"])
app.add_url_rule(routes["decimalBinarySM_route"], view_func= routes["decimalBinarySM_route_controller"])
app.add_url_rule(routes["binaryFixedPointFractionalDecimal_route"], view_func= routes["binaryFixedPointFractionalDecimal_route_controller"])