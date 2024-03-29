from flask.views import MethodView
from flask import request, render_template, redirect
from flask import flash
from src.functions import functionsHUB


class IndexController(MethodView):
    def get(self):
        return render_template('public/index.html')
    
    def post(self):
        binaryNumber = request.form['binaryNumber']
        flash(functionsHUB.binaryConversions(binaryNumber, 1))
        flash(binaryNumber)
        return redirect('/')
    
class BinaryToSmController(MethodView):
    def get(self):
        return render_template('public/binarioParaSM.html')
    
    def post(self):
        binaryNumber = request.form['binaryNumber']
        flash(functionsHUB.binaryConversions(binaryNumber, 2))
        flash(binaryNumber)
        return redirect('/binarioParaSM')
    
class BinaryToCTwoController(MethodView):
    def get(self):
        return render_template('public/binarioParaComplementoDois.html')
    
    def post(self):
        binaryNumber = request.form['binaryNumber']
        flash(functionsHUB.binaryConversions(binaryNumber, 3))
        flash(binaryNumber)
        return redirect('/binarioParaComplementoDois')
    
class DecimalToBinaryController(MethodView):
    def get(self):
        return render_template('public/decimalParaBinario.html')
    
    def post(self):
        decimalNumber = request.form['decimalNumber']
        flash(functionsHUB.decimalConversions(int(decimalNumber), 1))
        flash(decimalNumber)
        return redirect('/decimalParaBinario')