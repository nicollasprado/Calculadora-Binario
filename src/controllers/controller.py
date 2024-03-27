from flask.views import MethodView
from flask import request, render_template, redirect
from src.functions import index


class IndexController(MethodView):
    def get(self):
        return render_template('public/index.html')
    
    def post(self):
        binaryNumber = request.form['binaryNumber']
        binaryConversion = index.binaryConversions(binaryNumber)
        return binaryConversion