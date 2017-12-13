from flask import Flask, redirect, render_template, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    displayAll = True
    return render_template('displayninjas.html', displayAll=displayAll)

@app.route('/ninja/<color>')
def getColor(color):
    displayAll = False
    return render_template('displayninjas.html', color=color, displayAll=displayAll)

app.run(debug=True)