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
        bitsQuantity = request.form['bitsQuantity']
        flash(functionsHUB.decimalConversions(decimalNumber, 1, int(bitsQuantity)))
        flash(decimalNumber)
        flash(bitsQuantity)
        return redirect('/decimalParaBinario')
    


class DecimalToBinaryCTwoController(MethodView):
    def get(self):
        return render_template('public/decimalParaBinarioComplementoDois.html')
    
    def post(self):
        decimalNumber = request.form['decimalNumber']
        bitsQuantity = request.form['bitsQuantity']
        flash(functionsHUB.decimalConversions(decimalNumber, 2, int(bitsQuantity)))
        flash(decimalNumber)
        flash(bitsQuantity)
        return redirect('/decimalParaBinarioComplementoDois')
    


class DecimalToBinarySmController(MethodView):
    def get(self):
        return render_template('public/decimalParaBinarioSinalMagnitude.html')
    
    def post(self):
        decimalNumber = request.form['decimalNumber']
        bitsQuantity = request.form['bitsQuantity']
        flash(functionsHUB.decimalConversions(decimalNumber, 3, int(bitsQuantity)))
        flash(decimalNumber)
        flash(bitsQuantity)
        return redirect('/decimalParaBinarioSinalMagnitude')