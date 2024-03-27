from flask.views import MethodView
from flask import request, render_template, redirect
from src.functions import index


class IndexController(MethodView):
    def get(self):
        return render_template('public/index.html')
    
    def post(self):
        binarieNumber = request.form['binarieNumber']
        binarieConversion = index.binarieConversions(binarieNumber)
        return binarieConversion